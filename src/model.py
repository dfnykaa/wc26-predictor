import numpy as np
from src.data import TEAMS

def predict_match(team_a: str, team_b: str, noise: float = 0.15) -> tuple[str, float, float]:
    """
    Predict match winner based on team strength, FIFA rank, goals and historical data.
    Returns (winner, prob_a, prob_b)
    """
    a = TEAMS[team_a]
    b = TEAMS[team_b]

    def team_score(t: dict) -> float:
        rank_score = (200 - t["fifa_rank"]) / 200
        goal_score = t["avg_goals"] / 3.0
        defense_score = (3.0 - t["avg_conceded"]) / 3.0
        title_bonus = min(t["wc_titles"] * 0.03, 0.15)
        strength_score = t["strength"] / 100.0
        return (rank_score * 0.25 + goal_score * 0.2 + defense_score * 0.2 +
                strength_score * 0.3 + title_bonus * 0.05)

    score_a = team_score(a)
    score_b = team_score(b)

    score_a += np.random.normal(0, noise)
    score_b += np.random.normal(0, noise)

    total = score_a + score_b
    prob_a = score_a / total
    prob_b = score_b / total

    winner = team_a if score_a > score_b else team_b
    return winner, round(prob_a, 3), round(prob_b, 3)


def simulate_group(group: list[str]) -> dict:
    """Simulate group stage, return standings."""
    standings = {team: {"pts": 0, "gf": 0, "ga": 0, "gd": 0} for team in group}

    matches = [(group[i], group[j]) for i in range(len(group)) for j in range(i+1, len(group))]

    for team_a, team_b in matches:
        winner, prob_a, prob_b = predict_match(team_a, team_b, noise=0.12)

        a_stats = TEAMS[team_a]
        b_stats = TEAMS[team_b]
        goals_a = max(0, int(np.random.poisson(a_stats["avg_goals"] * prob_a * 1.5)))
        goals_b = max(0, int(np.random.poisson(b_stats["avg_goals"] * prob_b * 1.5)))

        if goals_a > goals_b:
            standings[team_a]["pts"] += 3
        elif goals_b > goals_a:
            standings[team_b]["pts"] += 3
        else:
            standings[team_a]["pts"] += 1
            standings[team_b]["pts"] += 1

        standings[team_a]["gf"] += goals_a
        standings[team_a]["ga"] += goals_b
        standings[team_b]["gf"] += goals_b
        standings[team_b]["ga"] += goals_a

    for team in standings:
        standings[team]["gd"] = standings[team]["gf"] - standings[team]["ga"]

    sorted_teams = sorted(
        standings.items(),
        key=lambda x: (x[1]["pts"], x[1]["gd"], x[1]["gf"]),
        reverse=True
    )
    return sorted_teams


def simulate_tournament(groups: dict, n_simulations: int = 10000) -> dict:
    """Run full tournament simulation N times, return win probabilities."""
    win_counts = {team: 0 for group in groups.values() for team in group}
    final_counts = {team: 0 for group in groups.values() for team in group}
    sf_counts = {team: 0 for group in groups.values() for team in group}

    for _ in range(n_simulations):
        qualifiers = {}
        for group_name, group_teams in groups.items():
            sorted_teams = simulate_group(group_teams)
            qualifiers[group_name] = [sorted_teams[0][0], sorted_teams[1][0]]

        group_names = list(groups.keys())
        r16_winners = []
        for i in range(0, len(group_names), 2):
            g1, g2 = group_names[i], group_names[i+1]
            w1, _, _ = predict_match(qualifiers[g1][0], qualifiers[g2][1], noise=0.1)
            w2, _, _ = predict_match(qualifiers[g2][0], qualifiers[g1][1], noise=0.1)
            r16_winners.extend([w1, w2])

        qf_winners = []
        for i in range(0, len(r16_winners), 2):
            w, _, _ = predict_match(r16_winners[i], r16_winners[i+1], noise=0.1)
            qf_winners.append(w)

        sf_winners = []
        for i in range(0, len(qf_winners), 2):
            w, _, _ = predict_match(qf_winners[i], qf_winners[i+1], noise=0.08)
            sf_winners.append(w)
            sf_counts[qf_winners[i]] += 1
            sf_counts[qf_winners[i+1]] += 1

        finalist_a, finalist_b = sf_winners[0], sf_winners[1]
        final_counts[finalist_a] += 1
        final_counts[finalist_b] += 1

        champion, _, _ = predict_match(finalist_a, finalist_b, noise=0.06)
        win_counts[champion] += 1

    results = {}
    for team in win_counts:
        results[team] = {
            "win_pct":    round(win_counts[team] / n_simulations * 100, 2),
            "final_pct":  round(final_counts[team] / n_simulations * 100, 2),
            "semi_pct":   round(sf_counts[team] / n_simulations * 100, 2),
            "strength":   TEAMS[team]["strength"],
            "fifa_rank":  TEAMS[team]["fifa_rank"],
        }

    return dict(sorted(results.items(), key=lambda x: x[1]["win_pct"], reverse=True))