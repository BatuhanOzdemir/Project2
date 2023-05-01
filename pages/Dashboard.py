import streamlit as st
import pandas as pd
import Home


df = st.session_state.table

st.title("Dashboard")

selection = st.sidebar.selectbox(label="Select the graph type",
                     options=("Line Chart","Bar Chart","Area Chart","Altair","Plotly","Vega-Lite"))

if selection 