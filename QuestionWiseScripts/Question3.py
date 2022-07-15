import pandas as pd

df = pd.read_csv("../Datasets/ques2.csv")
dfnew = df.rename(columns={"Price": "Close"})
dfnew.to_csv("../Datasets/ques3.csv", index=False)
