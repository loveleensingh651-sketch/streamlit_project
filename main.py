import streamlit as st

home_page = st.Page("project1/home.py",title="Home")
analysis_page = st.Page("project1/analysis.py", title="Analysis")
visualization_page = st.Page("project1/visualization.py", title="Visualization")
numpy_usage = st.Page("project1/numpy_usage.py", title="numpy usage")
insights = st.Page("project1/insights.py", title="Insight")

pg = st.navigation([home_page,
                    analysis_page, 
                    visualization_page,
                    numpy_usage,
                    insights])
pg.run()