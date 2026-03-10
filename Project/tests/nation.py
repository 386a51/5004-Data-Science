#a basic python script to check columns

import pandas as pd
import os


csvfile = os.path.join("..", "Trips_by_Distance.csv")
with open(csvfile, "r") as f:
	a=pd.read_csv(f)

csvfile = os.path.join("..", "Trips_Full_Data.csv")
with open(csvfile, "r") as f:
	b=pd.read_csv(f)



def check_unique_nation_values(nba):
	a = nba["Level"].unique()
	b = nba["Population Staying at Home"].unique()
	print(a)
	print(b)	



print("trips by distance")


check_unique_nation_values(a)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("trips full data")

check_unique_nation_values(b)
