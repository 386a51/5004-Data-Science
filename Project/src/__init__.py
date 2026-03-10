
csvfile = os.path.join("..", "Trips_by_Distance.csv")
with open(csvfile, "r") as f:
        nba=pd.read_csv(f)
