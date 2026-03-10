#a basic python script to get all csv file data easily

import pandas as pd
import os


csvfile = os.path.join("..", "Trips_by_Distance.csv")
with open(csvfile, "r") as f:
	nba=pd.read_csv(f)


#sets head to show all elements
pd.set_option("display.max.columns", None)
pd.options.display.max_columns



type(nba)
print("\n")
print("\n")
print("\n")
print("\n")

print(nba.shape)
print("\n")
print("\n")
print("\n")
print("\n")

print(len(nba))
print("\n")
print("\n")
print("\n")
print("\n")

print(nba.head())
print("\n")
print("\n")
print("\n")
print("\n")


#print(nba.iloc[1::5, :])

#for i, j in nba.iterrows():
#       print(i,j)
#       print(i)

nba.info()

print(nba.describe())
