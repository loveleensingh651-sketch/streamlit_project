import pandas as pd
import numpy as np
import streamlit as st
from project1.home import data
from project1.analysis import overall_marks

def normalize(marks):
    min1 = marks.min()
    max1 = marks.max()
    return ((marks-min1)/(max1-min1))
data1 = pd.DataFrame()
data1["gender"] = data["gender"].copy()

st.markdown("### Normalized form of scores", text_alignment="center")
data1["math score"] = data["math score"]
data1["math score normalized"] = normalize(data["math score"])
data1["reading score"] = data["reading score"]
data1["reading score normalized"] = normalize(data["reading score"])
data1["writing score"] = data["writing score"]
data1["writing score normalized"] = normalize(data["writing score"])
st.dataframe(data1, height=250)


def mean_std(scores):
    mean1 = np.mean(scores)
    std1 = np.std(scores)
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.metric(label=f"Mean score of {scores.name.split()[0]}",
                     value=f"{mean1:.2f}")
    with col2:
        with st.container(border=True):
            st.metric(label=f"Standard deviation of {scores.name.split()[0]}",
                        value=f"{std1:.2f}")

st.sidebar.subheader("To check (mean) and (std) :")

if st.sidebar.checkbox("Click to check maths details"):
    st.markdown("### Maths", text_alignment="center")
    mean_std(data1["math score"])
if st.sidebar.checkbox("Click to check reading details"):
    st.markdown("### Reading", text_alignment="center")
    mean_std(data1["reading score"])
if st.sidebar.checkbox("Click to check writing details"):
    st.markdown("### Writing", text_alignment="center")
    mean_std(data1["writing score"])


st.sidebar.subheader("Click to check grades of all total subjects")
if st.sidebar.checkbox("Click here"):
    st.subheader("Grades of students",text_alignment="center")
    overall_marks["Grades"] = np.where(overall_marks["average_marks"]>80,"A", 
                                       np.where(overall_marks["average_marks"]>60,"B",
                                                np.where(overall_marks["average_marks"]>40,"C","D")))
    st.dataframe(overall_marks)