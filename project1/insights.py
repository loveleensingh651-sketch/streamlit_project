import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from project1.home import data
from project1.analysis import overall_marks,gp2_groups

st.header("Insights Page")

#question 1
st.markdown("### 1. Does test preparation course improve marks?")
overall_marks["test preparation"] = data["test preparation course"]
fig1, ax1 = plt.subplots(figsize=(8,6))
ax1.grid(axis="y")
sns.violinplot(data=overall_marks, 
               x="test preparation", 
               y= "average_marks",
               inner="box")
ax1.set_xticklabels(["Not done", "Done"])
ax1.set_xlabel(xlabel="Test Preparation",fontsize=14)
ax1.set_ylabel(ylabel="Average marks",fontsize=14)
st.pyplot(fig1)

st.success("""
### Key Insights: 
* **Minimum marks**: minimum scores rose from ~30 to 40   
* **Density of marks**: More students scored between 60 to 100
* **Median Increase**: median increased from **65 to ~75**""")


st.markdown("### 2. Which subject has most variation in scores?")
# std_marks = pd.DataFrame(data[["math score","reading score", "writing score"]].std())
std_marks = data[["math score","reading score", "writing score"]].std().reset_index()
std_marks.columns = ["Subjects", "Standard deviation"]
st.dataframe(std_marks)

st.info("""
### Highest variation:  
#### Writing
* Overall variation in each subject is same 
""")


st.markdown("### 3. What percentage of students passed all three subjects?")
pass_st = overall_marks[overall_marks["average_marks"]>=40]
fail_st = overall_marks[overall_marks["average_marks"]<40]
total_st = overall_marks["average_marks"].count()
st.write(f""" passed students : **{len(pass_st)}** """)
st.write(f""" total students : **{total_st}** """)
st.success(f""" #### Percentage of passed students : {len(pass_st)/total_st*100}%""")


st.markdown("### 4. Is there correlation between maths and reading scores?")
fig2, ax1 = plt.subplots(figsize=(3,2.5))
sns.heatmap(data[["math score", "reading score"]].corr(),annot=True)
st.pyplot(fig2)
st.success("There is a positive correlation between these two")


st.markdown("### 5. Which group has highest average overall?")
st.dataframe(gp2_groups)

max_gp2_name = gp2_groups["overall average"].idxmax()
max_gp2_value = float(gp2_groups["overall average"].max())

col1, col2, col3 = st.columns(3)

with col2:
            with st.container(border=True):
                st.markdown(f"### TOP PERFORMING GROUP")
                st.metric(label=f"{max_gp2_name}", 
                        value=f"{max_gp2_value:.2f}")   