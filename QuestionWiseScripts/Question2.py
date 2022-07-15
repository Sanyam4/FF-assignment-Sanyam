import pandas as pd

df = pd.read_csv("../Datasets/German 10 YR Bund Futures Historical Data (2).csv")
df = df[["Date", "Open", "High", "Low", "Price", "Vol.", "Change %"]]
df.to_csv("../Datasets/ques2.csv", index=False)
