import sys
import pandas as pd

print("arguments", sys.argv)

day = int(sys.argv[1])
month = int(sys.argv[2])

head = pd.DataFrame({"day": [day], "month": [month]})

df = pd.DataFrame({
    "day": [1, 23, 412],
    "month": [1, 32, 3]
})

print(df.head())

# export parquet
df.to_parquet("output.parquet", index=False)

print(f"Running pipeline for day {day} and month {month}")