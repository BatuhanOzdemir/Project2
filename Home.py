import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Upload",page_icon="📤")
tab1,tab2,tab3,tab4 = st.tabs(["📤Upload","📊 Analyze","🔮 Predictions","🗳️ Polls"])

def createDataFrame(file):
    df = pd.read_excel(file)
    return df



def displayDataFrame(df):

    col1,col2,col3 = st.columns(3)
    col1.metric(label="Total Nr. of Employees",value=len(df.index))
    col2.metric(label="Average Age",value=df['Age'].mean())
    col3.metric(label="Average Salary",value=df['Monthly Gross Wage'].mean())
    st.experimental_data_editor(df)
    st.divider()



#A file loader to upload the excel files.
with tab1:
    st.subheader("File Upload")
    uploadedFiles = st.file_uploader(label="Upload the excel file to analyze", accept_multiple_files=True, type=["csv", "xlsx"], help="Only Excel files are allowed", key="uploadWidget")
    if uploadedFiles is None:
        st.warning("Please upload a file")
    elif  uploadedFiles is not None:
        if uploadedFiles not in st.session_state:
            st.session_state.uploadedFiles = uploadedFiles
        uploadButton = st.button(label="📤 Upload")
        if uploadButton and uploadedFiles is not None:
            st.info("Upload succesful. You can now analyze your data")
with tab2:
    if uploadedFiles is not None:
        with st.expander("Data Editors"):
            for file in uploadedFiles:
                df = createDataFrame(file)
                st.subheader("Data Editor "+file.name)
                displayDataFrame(df)
        with st.expander("Create a Graph"):
            df = uploadedFiles
            selectedFile = st.selectbox(label="Select a file",options=(file.name for file in uploadedFiles))
            for file in uploadedFiles:
                if file.name == selectedFile:
                    df = createDataFrame(file)
            graphType = st.selectbox(label="Select graph type",options=["Line chart","Area Chart","Bar Chart","Scatter Plot"])
            columns = df.select_dtypes(include='number').columns.tolist()
            xAxis = st.selectbox(label="Select data for the x axis",options=columns)
            yAxis = st.selectbox(label="Select data for the y axis",options=columns)
            createButton = st.button(label="Create Graph")
            if createButton:
                if graphType == 'Bar Chart':
                    fig = px.bar(df, x=xAxis, y=yAxis, color='country', barmode='group')
                else:
                    fig = px.scatter(df, x=xAxis, y=yAxis, color='country')
                if graphType and xAxis and yAxis:
                    st.plotly_chart(fig)
        with st.expander("Comparision Graphs"):
            for file in uploadedFiles:
                df = createDataFrame(file)

    else:
        st.warning("No file found")




