# app.py
# Streamlit visualization of Dr. Semmelweis data
# Code snippet assisted by ChatGPT

import streamlit as st
import pandas as pd
import altair as alt

# --- Title and Description ---
st.title("Higher Mortality in Clinic 1 Suggests a Connection Betwwen Unsanitary Staff and Maternal Death")
st.markdown("**Contributors:** Reet Verma, Nabila Yousfi, Tim Goncharov")
st.write("""
This dataset shows births and deaths in two clinics (1841–1849) at the Vienna General Hospital.  
In 1847, Dr. Ignaz Semmelweis introduced handwashing, dramatically reducing maternal deaths.  
Use the filters on the left to explore data for each clinic.
""")

# --- Load Data ---
df = pd.read_csv("yearly_deaths_by_clinic-1.csv")

# --- Calculate Mortality Rate ---
df["Mortality Rate (%)"] = (df["Deaths"] / df["Birth"]) * 100  # matches your CSV column

# --- Sidebar Filters ---
st.sidebar.header("Filters")
selected_clinic = st.sidebar.multiselect(
    "Select clinic(s):",
    options=df["Clinic"].unique(),
    default=df["Clinic"].unique()
)

filtered_df = df[df["Clinic"].isin(selected_clinic)]

# --- Visualization 1: Mortality Rate Over Time with Handwashing Marker ---
base = alt.Chart(filtered_df).encode(
    x="Year:O"
)

# Line chart
line = base.mark_line(point=True).encode(
    y="Mortality Rate (%):Q",
    color="Clinic:N",
    tooltip=["Year", "Clinic", "Mortality Rate (%)"]
)

# Vertical rule for 1847
rule = alt.Chart(pd.DataFrame({"Year": [1847]})).mark_rule(
    color="red",
    strokeDash=[4,4],
    size=2
).encode(
    x="Year:O"
)

# Text annotation
text = alt.Chart(pd.DataFrame({"Year": [1847], "label": ["1847: Handwashing Introduced"]})).mark_text(
    align="left",
    dx=5,
    dy=-10,
    color="red"
).encode(
    x="Year:O",
    y=alt.value(16),  # place above chart; adjust as needed
    text="label:N"
)

# Combine all
mortality_chart = alt.layer(line, rule, text).properties(
    title="Maternal Mortality Rate by Clinic (1841–1849)"
)

st.altair_chart(mortality_chart, use_container_width=True)


# --- Visualization 2: Total Deaths by Clinic ---
bar_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="Clinic:N",
        y="sum(Deaths):Q",
        color="Clinic:N",
        tooltip=["Clinic", "sum(Deaths)"]
    )
    .properties(title="Total Deaths by Clinic (1841–1849)")
)

st.altair_chart(bar_chart, use_container_width=True)


# --- Findings ---
st.subheader("Key Findings")
st.write("""
- In **Clinic 1**, mortality rates were much higher than Clinic 2 before 1847.  
- After handwashing was introduced (1847), deaths in Clinic 1 dropped dramatically.  
- Clinic 2, run by midwives, had consistently lower death rates, showing that hygiene practices were critical.  
- Overall, this dataset provides one of the earliest examples of data-driven public health intervention.
""")

st.caption("Data visualization project for Streamlit Cloud deployment.")
