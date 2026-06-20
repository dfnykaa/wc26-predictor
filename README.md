# 🏆 FIFA World Cup 2026 Predictor


## 🔮 Latest Prediction (10,000 simulations)

| # | Team | Win % | Final % | Semi % |
|---|------|--------|---------|--------|
| 🥇 | Argentina | ~24% | ~28% | ~39% |
| 🥈 | Belgium | ~15% | ~34% | ~45% |
| 🥉 | France | ~13% | ~16% | ~26% |
| 4 | Brazil | ~10% | ~14% | ~22% |
| 5 | Spain | ~9% | ~12% | ~28% |

## ⚙️ How it works

The model simulates the entire World Cup **10,000 times** and calculates the probability of each team winning based on:

- 🎯 **FIFA Ranking** — current world ranking
- ⚽ **Average goals scored / conceded** — attack & defense strength
- 🏆 **World Cup titles** — historical pedigree bonus
- 💪 **Team strength rating** — composite score
- 🎲 **Controlled randomness** — upsets happen!

Each simulation runs:
1. Group stage (round robin)
2. Round of 16
3. Quarter-finals
4. Semi-finals
5. Final

## 🚀 Run it yourself

```bash
git clone https://github.com/yourusername/wc2026-predictor
cd wc2026-predictor
pip install -r requirements.txt
python main.py
```

## 📊 Output

- Terminal output with top 10 predicted champions
- Bar charts saved to `/output/`
- Single match predictor for key matchups

## 📦 Tech Stack

- `Python 3.10+`
- `NumPy` — Monte Carlo simulation
- `Pandas` — data handling
- `Matplotlib` — visualization

## 📁 Project Structure

```
wc2026-predictor/
├── main.py           # Entry point
├── src/
│   ├── data.py       # Team stats & group draw
│   ├── model.py      # Prediction & simulation logic
│   └── visualize.py  # Charts & graphs
└── output/           # Generated charts
```