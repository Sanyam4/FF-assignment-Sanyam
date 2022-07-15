import numpy as np
import pandas as pd

data = pd.read_csv("../Datasets/ques3.csv", index_col=False)
data = data.iloc[::-1]


high_low = data["High"] - data["Low"]
high_close = np.abs(data["High"] - data["Close"].shift())
low_close = np.abs(data["Low"] - data["Close"].shift())

ranges = pd.concat([high_low, high_close, low_close], axis=1)
true_range = np.max(ranges, axis=1)


atr = true_range.rolling(14).mean()
ATR = pd.DataFrame(atr)

final = pd.merge(data, ATR, left_index=True, right_index=True)
final.rename(columns={0: "ATR(14)"}, inplace=True)
print(final)
final.to_csv("../Datasets/ques4.csv", index=False)
