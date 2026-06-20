import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.data import GROUPS, get_teams_df
from src.model import simulate_tournament, predict_match
from src.visualize import plot_win_probabilities, plot_strength_radar

def print_banner():
    print("\033[38;5;197m")
    print(" 🏆  FIFA World Cup 2026 Predictor  🏆")

def print_results(results: dict):
    print("\n\033[1m\033[38;5;226m  🏆 TOP 10 PREDICTED CHAMPIONS\033[0m")
    print(f"  {'#':<4} {'Team':<18} {'Win %':<10} {'Final %':<12} {'Semi %':<10} {'Rank'}")
    print("  " + "─" * 60)

    medals = ["🥇", "🥈", "🥉"]
    for i, (team, data) in enumerate(list(results.items())[:10]):
        medal = medals[i] if i < 3 else f"  {i+1}."
        rank = data['fifa_rank']
        print(f"  {medal:<4} {team:<18} {data['win_pct']:<10.1f} {data['final_pct']:<12.1f} {data['semi_pct']:<10.1f} #{rank}")

    print()

def predict_single_match():
    print("\n\033[38;5;117m  ⚽ SINGLE MATCH PREDICTOR\033[0m")
    print("  Simulating key potential matches...\n")

    matchups = [
        ("Argentina", "France"),
        ("Brazil", "England"),
        ("Spain", "Germany"),
        ("Portugal", "Netherlands"),
    ]

    for team_a, team_b in matchups:
        wins_a, wins_b = 0, 0
        for _ in range(1000):
            w, _, _ = predict_match(team_a, team_b, noise=0.1)
            if w == team_a: wins_a += 1
            else: wins_b += 1

        prob_a = wins_a / 10
        prob_b = wins_b / 10
        fav = team_a if prob_a > prob_b else team_b
        print(f"  {team_a} vs {team_b}")
        print(f"    → \033[38;5;197m{fav}\033[0m wins  ({team_a}: {prob_a:.0f}% | {team_b}: {prob_b:.0f}%)\n")

if __name__ == "__main__":
    print_banner()

    print("  🔄 Running 10,000 tournament simulations...")
    results = simulate_tournament(GROUPS, n_simulations=10000)

    print_results(results)
    predict_single_match()

    print("  📊 Generating charts...\n")
    os.makedirs("output", exist_ok=True)
    plot_win_probabilities(results, "output/wc2026_predictions.png")
    plot_strength_radar(results, "output/wc2026_top8.png")

    print("\n  \033[38;5;82m✅ Done! Charts saved to /output/\033[0m\n")