import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

data = pd.read_csv("StudentsPerformance.csv")

r,c = data.shape


st.header("Dataset of StudentsPerformance",text_alignment="center")

st.sidebar.header("Details of Dataset")
st.sidebar.write("No. of rows : ", r)
st.sidebar.write("No. of columns : ", c)

st.dataframe(data, height=250)

filtered_value = pd.DataFrame()
#for selections of columns
col = st.sidebar.multiselect("Select Colums to show", ["name","gender","test preparation course","math score", "writing score", "reading score"])

#inserting columns

if "name" in col:
    filtered_value["name"] = data["name"]

if "gender" in col:
    filtered_value["gender"] = data["gender"]
    
if "test preparation course" in col:
    filtered_value["test preparation course"] = data["test preparation course"]
    
if "math score" in col:
    filtered_value["math score"] = data["math score"]

if "writing score" in col:
    filtered_value["writing score"] = data["writing score"]

if "reading score" in col:
    filtered_value["reading score"] = data["reading score"]

if "gender" in col:
    gender_value = st.sidebar.radio("Select gender", ["both","male", "female"])
    if gender_value == "both":
        pass
    elif gender_value == "male":
        filtered_value = filtered_value[filtered_value["gender"]=="male"]
    else:
        filtered_value = filtered_value[filtered_value["gender"]=="female"]

if "test preparation course" in col:
    test_preparation_value = st.sidebar.radio("Select value to filter", ["both","none", "completed"])
    if test_preparation_value == "both":
        pass
    elif test_preparation_value == "none":
        filtered_value = filtered_value[filtered_value["test preparation course"]=="none"]
    else:
        filtered_value = filtered_value[filtered_value["test preparation course"]=="completed"]


st.sidebar.write("Description of Data:")
st.sidebar.write(data.describe())
st.sidebar.write("No. of Null:")
st.sidebar.dataframe(data.isnull().sum())

st.markdown("### Filtered data")

#display of filtered columns
st.dataframe(filtered_value)    

