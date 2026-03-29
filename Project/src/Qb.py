import numpy as np
import time
import pandas as pd
import os
import math
import matplotlib.pyplot as plt

def comparison():
	csvfile = os.path.join("..", "Trips_Full_Data.csv")
	with open(csvfile, "r") as f:
        	nba=pd.read_csv(f)


	#create dataset object of just population staying at home and date
	pd.dataset1 =[]
	pd.dataset2 =[]
	trips_10_25 = nba["Trips 10-25 Miles"]
	trips_50_100 = nba["Trips 50-100 Miles"]
	date = nba["Date"]

	#creates 2 datasets for each feild
	frame1 = (trips_10_25, date)
	frame2 = (trips_50_100, date)
	dataset1 = pd.concat(frame1, axis=1)
	dataset2 = pd.concat(frame2, axis=1)

	#filters the dates that are smaller than 10,000,000 creating a new dataset
	filtered_10_25 =dataset1[dataset1["Trips 10-25 Miles"] > 10000000]
	filtered_50_100 = dataset2[dataset2["Trips 50-100 Miles"] > 10000000]



	print(filtered_50_100.head())
	print(filtered_10_25.head())


	plt.scatter(filtered_10_25["Date"], filtered_10_25["Trips 10-25 Miles"], label="10-25 Miles")
	plt.scatter(filtered_50_100["Date"], filtered_50_100["Trips 50-100 Miles"], label="50-100 Miles")

	plt.xlabel("Date")
	plt.ylabel("Number of Trips")
	plt.title("Comparison of Trip Distances (>10M)")
	plt.legend()
	plt.xticks(rotation=45)
	plt.show()



comparison()
