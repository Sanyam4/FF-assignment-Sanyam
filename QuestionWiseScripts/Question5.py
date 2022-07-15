## as moving average 20 is considered as most important moving average so will consider 20 previous point standard deviation
import pandas as pd

print("Enter the interval for which deviation has to be calculated :")
n = input()


def standardDeviation(n):

    data = pd.read_csv("../Datassets/ques4.csv")
    close_list = data["Close"]
    atr_list = data["ATR(14)"]

    movingstddevclose = close_list.rolling(n).std()

    movingstddevatr = atr_list.rolling(n).std()

    data["movingstddevclose"] = movingstddevclose
    data["movingstddevatr"] = movingstddevatr

    data.to_csv("../Datasets/ques5.csv", index=False)
