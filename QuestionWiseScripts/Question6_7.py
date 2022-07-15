import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("../Datasets/ques5.csv")

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date")

date_index = df.set_index("Date")
dt_breaks = pd.date_range(
    start=date_index.index[0], end=date_index.index[-1]
).difference(date_index.index)

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.30,
    subplot_titles=("OHLC", "ATR/STDDEV"),
    row_width=[1, 3],
)
fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])  # hide dates with no values
fig.add_trace(
    go.Candlestick(
        x=date_index.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        showlegend=False,
        name="OHLC",
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=date_index.index,
        y=date_index["movingstddevclose"],
        line=dict(color="red", width=2),
        name="STDDEV(CLS)",
    ),
    row=2,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=date_index.index,
        y=date_index["movingstddevatr"],
        line=dict(color="blue", width=2),
        name="STDDEV(ATR)",
    ),
    row=2,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=date_index.index,
        y=date_index["ATR(14)"],
        line=dict(color="green", width=2),
        name="ATR(14)",
    ),
    row=2,
    col=1,
)

fig.show()
