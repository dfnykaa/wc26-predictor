import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

DARK_BG = "#0d1117"
CARD_BG = "#161b22"
ACCENT = "#F75C7E"
ACCENT2 = "#58a6ff"
TEXT = "#e6edf3"
MUTED = "#8b949e"
GREEN = "#3fb950"
YELLOW = "#d29922"

def style_ax(ax):
    ax.set_facecolor(CARD_BG)
    ax.tick_params(colors=TEXT)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor("#30363d")

def plot_win_probabilities(results: dict, output_path: str):
    top = dict(list(results.items())[:16])
    teams = list(top.keys())
    win_pcts = [top[t]["win_pct"] for t in teams]
    final_pcts = [top[t]["final_pct"] for t in teams]
    semi_pcts = [top[t]["semi_pct"] for t in teams]

    fig, axes = plt.subplots(1, 3, figsize=(20, 8))
    fig.patch.set_facecolor(DARK_BG)
    fig.suptitle("🏆 FIFA World Cup 2026 — Prediction", color=TEXT, fontsize=20, fontweight="bold", y=1.02)

    datasets = [
        (axes[0], win_pcts, "🏆 Champion", ACCENT),
        (axes[1], final_pcts, "🥈 Reach Final", ACCENT2),
        (axes[2], semi_pcts, "🥉 Reach Semi-Final", GREEN),
    ]

    for ax, data, title, color in datasets:
        style_ax(ax)
        bars = ax.barh(teams[::-1], data[::-1], color=color, alpha=0.85, height=0.6)
        ax.set_title(title, color=TEXT, fontsize=13, fontweight="bold", pad=10)
        ax.set_xlabel("Probability (%)", color=MUTED, fontsize=10)

        for bar, val in zip(bars, data[::-1]):
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                    f"{val:.1f}%", va="center", ha="left", color=TEXT, fontsize=9)

        ax.set_xlim(0, max(data) * 1.25)
        ax.tick_params(axis="y", labelcolor=TEXT, labelsize=9)
        ax.tick_params(axis="x", labelcolor=MUTED, labelsize=8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  ✅ Chart saved: {output_path}")


def plot_strength_radar(results: dict, output_path: str):
    top8 = list(results.keys())[:8]

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(DARK_BG)
    style_ax(ax)

    colors = [ACCENT, ACCENT2, GREEN, YELLOW, "#bc8cff", "#ff7b72", "#79c0ff", "#56d364"]
    x = np.arange(len(top8))
    width = 0.35

    win_vals = [results[t]["win_pct"] for t in top8]
    final_vals = [results[t]["final_pct"] for t in top8]

    bars1 = ax.bar(x - width/2, win_vals, width, label="Win %", color=ACCENT, alpha=0.85)
    bars2 = ax.bar(x + width/2, final_vals, width, label="Final %", color=ACCENT2, alpha=0.85)

    ax.set_title("🏆 Top 8 Contenders — Champion vs Final Probability", color=TEXT, fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(top8, color=TEXT, fontsize=10)
    ax.set_ylabel("Probability (%)", color=MUTED)
    ax.legend(facecolor=CARD_BG, labelcolor=TEXT, edgecolor="#30363d")

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f"{bar.get_height():.1f}%", ha="center", va="bottom", color=TEXT, fontsize=8)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f"{bar.get_height():.1f}%", ha="center", va="bottom", color=TEXT, fontsize=8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=DARK_BG)
    plt.close()
    print(f"  ✅ Chart saved: {output_path}")