import numpy as np
import time
import pandas as pd
import os
import math


def converttoeng(date):
	a = date.split("/")
	return a[1] + "/" + a[0] + "/" + a[2]
	

def Travaling_analysis():
	csvfile = os.path.join("..", "Trips_by_Distance.csv")
	with open(csvfile, "r") as f:
        	nba=pd.read_csv(f)


	#create dataset object of just population staying at home and date
	dataset = pd.array(["Clean Data"])
	PSaH = nba["Population Staying at Home"]
	Level = nba["Level"]
	date = nba["Date"]
	frames = (PSaH, date, Level)
	dataset = pd.concat(frames, axis=1)


	#cleans date from State and National to english time
	dataset["Clean Date"] = dataset.apply(lambda row: converttoeng(row["Date"]) if row["Level"] == "County" or row["Level"] == "State" else row["Date"], axis=1)

	#removes unnecisary feilds	
	dataset = dataset.drop("Level", axis="columns")
	dataset = dataset.drop("Date", axis="columns")


#	print(dataset.sum())
	print(dataset.head)
#	print(dataset.dtypes)

	a = dataset.groupby(["Clean Date"])["Population Staying at Home"].mean()
	print(a.head)

Travaling_analysis()
