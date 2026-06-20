import pandas as pd
import numpy as np

# FIFA Rankings
TEAMS = {
    # Group A
    "Brazil":      {"fifa_rank": 5,  "avg_goals": 2.1, "avg_conceded": 0.8, "wc_titles": 5, "strength": 92},
    "Germany":     {"fifa_rank": 12, "avg_goals": 1.9, "avg_conceded": 1.0, "wc_titles": 4, "strength": 87},
    "Serbia":      {"fifa_rank": 33, "avg_goals": 1.4, "avg_conceded": 1.2, "wc_titles": 0, "strength": 72},
    "Japan":       {"fifa_rank": 18, "avg_goals": 1.5, "avg_conceded": 1.1, "wc_titles": 0, "strength": 76},
    # Group B
    "France":      {"fifa_rank": 2,  "avg_goals": 2.2, "avg_conceded": 0.9, "wc_titles": 2, "strength": 93},
    "Argentina":   {"fifa_rank": 1,  "avg_goals": 2.3, "avg_conceded": 0.7, "wc_titles": 3, "strength": 96},
    "Poland":      {"fifa_rank": 22, "avg_goals": 1.3, "avg_conceded": 1.3, "wc_titles": 0, "strength": 70},
    "Ecuador":     {"fifa_rank": 44, "avg_goals": 1.2, "avg_conceded": 1.4, "wc_titles": 0, "strength": 65},
    # Group C
    "Spain":       {"fifa_rank": 6,  "avg_goals": 2.0, "avg_conceded": 0.8, "wc_titles": 1, "strength": 91},
    "England":     {"fifa_rank": 4,  "avg_goals": 1.9, "avg_conceded": 0.9, "wc_titles": 1, "strength": 89},
    "USA":         {"fifa_rank": 13, "avg_goals": 1.5, "avg_conceded": 1.1, "wc_titles": 0, "strength": 77},
    "Iran":        {"fifa_rank": 22, "avg_goals": 1.1, "avg_conceded": 1.2, "wc_titles": 0, "strength": 68},
    # Group D
    "Netherlands": {"fifa_rank": 7,  "avg_goals": 1.9, "avg_conceded": 0.9, "wc_titles": 0, "strength": 88},
    "Portugal":    {"fifa_rank": 6,  "avg_goals": 2.1, "avg_conceded": 0.9, "wc_titles": 0, "strength": 90},
    "Mexico":      {"fifa_rank": 15, "avg_goals": 1.5, "avg_conceded": 1.1, "wc_titles": 0, "strength": 75},
    "Senegal":     {"fifa_rank": 20, "avg_goals": 1.4, "avg_conceded": 1.0, "wc_titles": 0, "strength": 74},
    # Group E
    "Belgium":     {"fifa_rank": 3,  "avg_goals": 2.0, "avg_conceded": 0.8, "wc_titles": 0, "strength": 90},
    "Croatia":     {"fifa_rank": 10, "avg_goals": 1.7, "avg_conceded": 1.0, "wc_titles": 0, "strength": 83},
    "Morocco":     {"fifa_rank": 14, "avg_goals": 1.3, "avg_conceded": 0.8, "wc_titles": 0, "strength": 78},
    "Canada":      {"fifa_rank": 41, "avg_goals": 1.2, "avg_conceded": 1.4, "wc_titles": 0, "strength": 64},
    # Group F
    "Uruguay":     {"fifa_rank": 17, "avg_goals": 1.6, "avg_conceded": 0.9, "wc_titles": 2, "strength": 79},
    "South Korea": {"fifa_rank": 23, "avg_goals": 1.4, "avg_conceded": 1.1, "wc_titles": 0, "strength": 72},
    "Ghana":       {"fifa_rank": 60, "avg_goals": 1.1, "avg_conceded": 1.3, "wc_titles": 0, "strength": 62},
    "Switzerland": {"fifa_rank": 19, "avg_goals": 1.5, "avg_conceded": 0.9, "wc_titles": 0, "strength": 76},
    # Group G
    "Colombia":    {"fifa_rank": 11, "avg_goals": 1.7, "avg_conceded": 1.0, "wc_titles": 0, "strength": 81},
    "Denmark":     {"fifa_rank": 21, "avg_goals": 1.6, "avg_conceded": 0.9, "wc_titles": 0, "strength": 77},
    "Tunisia":     {"fifa_rank": 30, "avg_goals": 1.1, "avg_conceded": 1.2, "wc_titles": 0, "strength": 65},
    "Australia":   {"fifa_rank": 25, "avg_goals": 1.3, "avg_conceded": 1.2, "wc_titles": 0, "strength": 70},
    # Group H
    "Italy":       {"fifa_rank": 9,  "avg_goals": 1.7, "avg_conceded": 0.8, "wc_titles": 4, "strength": 85},
    "Nigeria":     {"fifa_rank": 40, "avg_goals": 1.3, "avg_conceded": 1.3, "wc_titles": 0, "strength": 67},
    "Saudi Arabia":{"fifa_rank": 56, "avg_goals": 1.0, "avg_conceded": 1.5, "wc_titles": 0, "strength": 58},
    "Chile":       {"fifa_rank": 35, "avg_goals": 1.4, "avg_conceded": 1.2, "wc_titles": 0, "strength": 69},
}

GROUPS = {
    "A": ["Brazil", "Germany", "Serbia", "Japan"],
    "B": ["France", "Argentina", "Poland", "Ecuador"],
    "C": ["Spain", "England", "USA", "Iran"],
    "D": ["Netherlands", "Portugal", "Mexico", "Senegal"],
    "E": ["Belgium", "Croatia", "Morocco", "Canada"],
    "F": ["Uruguay", "South Korea", "Ghana", "Switzerland"],
    "G": ["Colombia", "Denmark", "Tunisia", "Australia"],
    "H": ["Italy", "Nigeria", "Saudi Arabia", "Chile"],
}

def get_teams_df():
    return pd.DataFrame(TEAMS).T.reset_index().rename(columns={"index": "team"})