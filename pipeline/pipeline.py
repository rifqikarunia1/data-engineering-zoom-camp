import sys

import pandas as pd

print("arguments", sys.argv)

day = int(sys.argv[1])
month = int(sys.argv[2])

head = pd.DataFrame({"day": [day], "month": [month]})
# head.to_csv("output.csv", index=False)

print(head.head())  

df = pd.DataFrame({"day": [1,23,412], "month": [1,32,3]})

print(df.head())

print(f"Running pipeline for day {day} and month {month}")