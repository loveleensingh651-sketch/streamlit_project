import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from project1.home import data
from project1.analysis import overall_marks,gp2_groups

# st.markdown("## Visual Representation of the data", text_alignment="center")

grid_style = dict(color="#7e9296", linestyle="dashed", alpha=0.8)

#distribution by histogram 
st.sidebar.markdown("#### Distribution of marks")
if st.sidebar.checkbox("Click here for histogram"):        
        st.subheader("Distribution Of Marks", text_alignment="center")
        fig1, ax1 = plt.subplots(figsize = (10,5.5))
        ax1.hist(overall_marks["total_marks"]/3, 
                color="#20b8d6", 
                edgecolor="black",
                bins=9)
        ax1.set_xlabel("No. of students",size=14)
        ax1.set_ylabel("Total marks of student",size=14)

        ax1.set_xticks(range(0,101, 10))
        ax1.grid(visible=True, axis="y", **grid_style)


        st.pyplot(fig1)

st.sidebar.markdown("#### Marks Comparison by gender")
if st.sidebar.checkbox("Click here for boxplot"):
        st.markdown("### Marks comparision by gender",text_alignment="center")
        fig2, ax1 = plt.subplots(figsize=(9,5.5))
        female_marks =  np.array(overall_marks["average_marks"][overall_marks["gender"] == "female"])
        male_marks =  np.array(overall_marks["average_marks"][overall_marks["gender"] == "male"])
        sns.boxplot([female_marks,male_marks])
        ax1.set_xticklabels(["female", "male"])
        ax1.set_xlabel("gender",size = 14)
        ax1.set_ylabel("average marks",size = 14)
        st.pyplot(fig2)


correlated_data = data[["math score", "reading score", "writing score"]].corr()


st.sidebar.markdown("#### Correlation between subjects")
if st.sidebar.checkbox("Click here for heatmap"):
        st.markdown("### Correlation between subjects", text_alignment="center")
        fig3, ax1 = plt.subplots(figsize = (10,5.5))
        sns.heatmap(correlated_data, 
                    annot=True, 
                    edgecolor="black")

        st.pyplot(fig3)


st.sidebar.markdown("#### Pass/Fail Analysis")
if st.sidebar.checkbox("Click here for Pie chart"):
        st.markdown("### Pass/Fail Pie chart",text_alignment="center")
        fig4, ax1 = plt.subplots(figsize = (7.5,1.6))

        pass_count = len(np.array(overall_marks[overall_marks["average_marks"]>=40]["average_marks"]))
        fail_count = len(np.array(overall_marks[overall_marks["average_marks"]<40]["average_marks"]))
        total_count = pass_count+fail_count
        pass_percentage = pass_count/total_count*100
        pass_fail_values = [pass_count,fail_count]


        plt.pie(pass_fail_values,
                labels=["(Pass)","(Fail)"],
                autopct="%.2f%%",
                pctdistance=1.55,
                labeldistance=2.08,
                explode=[0.0,0.1]
                )

        st.pyplot(fig4)
        
        with st.container(border=True):
                col1,col2,col3 = st.columns(3)
                col1.metric(label="Total Students",
                                value=f"{total_count}")
                col2.metric(label="Pass Rate", 
                                value=f"{pass_percentage}%")
                col3.metric(label="Failed Students",
                                value=f"{fail_count}",
                                delta=f"Need attention",
                                delta_color="red",
                                delta_arrow="down")


st.sidebar.markdown("#### Average Score by Each Group")
if st.sidebar.checkbox("Click here for barplot"):
        st.markdown("### Average Score **(Each Group)** ", text_alignment="center")
        fig5, ax1 = plt.subplots(figsize=(8,5))
        sns.barplot(data=gp2_groups, x="race/ethnicity", y="overall average")
        ax1.set_xlabel("Groups",size=14)
        ax1.set_ylabel("overall marks", size=14)


        st.pyplot(fig5)
