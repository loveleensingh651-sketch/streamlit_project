import streamlit as st
import numpy as np
import pandas as pd
from project1.home import data


st.header("Analysis Page")
# group of various subjects
gp_groups = data.groupby("race/ethnicity").agg(avg_marks_maths=("math score","mean"),
                                                 avg_marks_reading=("reading score", "mean"), 
                                                avg_marks_writing=("writing score", "mean"))

#group average of overall   
gp2_groups = pd.DataFrame(np.mean(gp_groups, axis=1),columns=["overall average"])

# to select which data to get by group 
col_values = st.sidebar.multiselect("Select group by data to average",["various subject wise", "overall"])


if "various subject wise" in col_values:
    # filtered_value2 = gp_groups
    st.markdown("### Average by groups in various subjects")
    st.dataframe(gp_groups)

# two ifs bcoz of multiselect i saw on google
if "overall" in col_values:
    # filtered_value2 = gp2_groups
    st.markdown("#### Overall Average by groups **(Of all subjects)**")
    st.dataframe(gp2_groups)

# st.dataframe(filtered_value2)
#kpi
max_gp2_value = float(gp2_groups["overall average"].max())
# max_gp2_name = str(gp2_groups[gp2_groups["overall average"]==max_gp2_value].index)
max_gp2_name = gp2_groups["overall average"].idxmax()

# these ideas and codes were searched from google
min_gp2_value = float(gp2_groups["overall average"].min())
min_gp2_name = gp2_groups["overall average"].idxmin()

gp2_grand_average = gp2_groups["overall average"].mean()
max_score_delta = max_gp2_value-gp2_grand_average
min_score_delta = gp2_grand_average-min_gp2_value

col1, col2, col3 = st.columns(3)

if len(col_values)>0:
    with col1: 
        with st.container(border=True):
            st.markdown(f"### TOP PERFORMING")
            st.metric(label=f"Group : {max_gp2_name}", 
                    value=f"{max_gp2_value:.2f}",
                    delta=f"+{max_score_delta:.2f} vs average")
    with col2:
        with st.container(border=True):
            st.markdown("### OVERALL AVERAGE")
            st.metric(label="Overall Average",
                    value=f"{gp2_grand_average}")
    with col3:
        with st.container(border=True):
            st.markdown("### LEAST PERFORMING")
            st.metric(label=f"Group:{min_gp2_name}",
                    value=f"{min_gp2_value:.2f}",
                    delta=f"-{min_score_delta:.2f} vs average")


overall_marks = pd.DataFrame()

overall_marks["name"] = data["name"]
overall_marks["gender"] = data["gender"]


overall_marks["total_marks"] = data[["math score", "reading score","writing score"]].sum(axis=1)
overall_marks["average_marks"] = overall_marks["total_marks"]/3

top_ten = pd.DataFrame()
top_ten = overall_marks.sort_values("average_marks",ascending=False).head(10)


#pass/fail
st.sidebar.markdown("#### Click to see Pass/Fail Students")

if st.sidebar.checkbox("Click Here"):
    results = st.sidebar.radio("Which result to see", ["Pass","Fail"])
    if results == "Pass":
        st.markdown("### Marks greater than equals to 40 **(Pass)**")
        pass_fail_result = (overall_marks[overall_marks["average_marks"]>=40])
    else:
        st.markdown("### Marks less than 40 **(Fail)**")
        pass_fail_result = (overall_marks[overall_marks["average_marks"]<40])
    st.dataframe(pass_fail_result)


if st.sidebar.checkbox("Show Top 10 students"):
    st.markdown("### Top 10 Students")

    st.dataframe(top_ten,height=300)

    with st.container(border=True):
        st.metric(label=f"Topper is {top_ten["total_marks"].idxmax()} ID",
                value=f"{top_ten["total_marks"].max()}",
                delta=f"+{(top_ten["total_marks"].max()-top_ten["total_marks"].min())} vs 10th rank")
                #pass/fail
