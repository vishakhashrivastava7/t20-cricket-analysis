import matplotlib.pyplot as plt
import pandas as pd

def plot_top_batsmen(df):
    top_batsmen = df.groupby("batter")["runs"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,5))
    top_batsmen.plot(kind="bar", color="skyblue")
    plt.title("Top 10 Batsmen by Total Runs")
    plt.xlabel("Batsman")
    plt.ylabel("Total Runs")
    plt.tight_layout()
    plt.show()

def plot_team_totals(df):
    team_runs = df.groupby("team")["runs"].sum().sort_values(ascending=False)
    plt.figure(figsize=(12,5))
    team_runs.plot(kind="bar", color="lightgreen")
    plt.title("Team-wise Total Runs")
    plt.xlabel("Team")
    plt.ylabel("Total Runs")
    plt.tight_layout()
    plt.show()

def plot_yearwise_totals(df):
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    year_runs = df.groupby("year")["runs"].sum().sort_index()
    plt.figure(figsize=(10,5))
    year_runs.plot(kind="line", marker="o", color="coral")
    plt.title("Year-wise Total Runs")
    plt.xlabel("Year")
    plt.ylabel("Total Runs")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("t20_data.csv")
    plot_top_batsmen(df)
    plot_team_totals(df)
    plot_yearwise_totals(df)
