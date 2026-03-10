#a basic python script to get all csv file data easily

import pandas as pd
import os

pd.set_option("display.max.columns", None)
pd.options.display.max_columns

csvfile = os.path.join("..", "Trips_by_Distance.csv")
with open(csvfile, "r") as f:
	a=pd.read_csv(f)

csvfile = os.path.join("..", "Trips_Full_Data.csv")
with open(csvfile, "r") as f:
	b=pd.read_csv(f)


#sets head to show all elements
pd.set_option("display.max.columns", None)
pd.options.display.max_columns

def analyse_data(nba):

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

print("trips by distance")

analyse_data(a)
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

analyse_data(b)
