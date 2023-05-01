import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt



#A file loader to upload the excel files.
st.title("HR Analytics"+":bar_chart:")
uploadedFile = st.file_uploader(label="Upload the excel file to analyze", key="uploadWidget")


@st.cache_data
def createDataFrame(uploadedFile):
    df = pd.read_excel(uploadedFile)
    return df


if st.button(label="Analyze"):
    table = createDataFrame(uploadedFile)
    if table not in st.session_state:
        st.session_state.table = table
    st.dataframe(table)








