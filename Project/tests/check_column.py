#a basic python script to check columns

import pandas as pd
import os


csvfile = os.path.join("..", "Trips_by_Distance.csv")
with open(csvfile, "r") as f:
	a=pd.read_csv(f)

csvfile = os.path.join("..", "Trips_Full_Data.csv")
with open(csvfile, "r") as f:
	b=pd.read_csv(f)



def check_column(nba):
	
	



print("trips by distance")

check_column(a)
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

check_column(b)
