import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.set_page_config(layout="wide")
st.title("German 10-Year Bund Futures")
if "main_dataset" not in st.session_state:
    st.session_state["main_dataset"] = pd.read_csv("Datasets/ques5.csv")
    st.session_state["close"] = st.session_state["main_dataset"]["Close"]
    st.session_state["atr"] = st.session_state["main_dataset"]["ATR(14)"]

########### PART - 5 : Calculate Moving Standard Deviation ################
n = st.number_input(
    "Set interval for moving standard deviation (in days)",
    min_value=1,
    step=1,
    max_value=200,
    value=1,
)
df = st.session_state["main_dataset"]
movingstddevclose = st.session_state["main_dataset"]["Close"].rolling(n).std()
movingstddevatr = st.session_state["main_dataset"]["ATR(14)"].rolling(n).std()
df["movingstddevclose"] = movingstddevclose
df["movingstddevatr"] = movingstddevatr
###########################################################################

########## PART - 6,7 : Charting ##########################################
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
        opacity=0.7,
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

fig.update_layout(width=1100, height=700)

st.plotly_chart(fig)
############################################################################
