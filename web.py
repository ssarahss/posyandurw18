import streamlit as st
import pandas as pd
import numpy as np

# Sample data recreated manually from the image
data = {
    "no": list(range(1, 31)),
    "age": [49, 59, 63, 60, 61, 61, 63, 57, 69, 58, 66, 57, 63, 60, 66, 63, 57, 66, 75, 56, 65, 63, 62, 60, 75, 63, 65, 63, 63, 63],
    "height": [147.5, 149, 52.4, 144.9, 151.5, 150, 152.7, 152.5, 155, 136.7, 152.7, 157, 158, 145.2, 146.5, 146.5, 151.6, 148.5, 147.6, 147.6,
               146, 144, 144, 144.8, 156.5, 138.5, 147, 145.9, 150, 148.5],
    "weight": [57.8, 52.4, 47.7, 42.4, 55.6, 69.8, 70.9, 56.2, 52.8, 45.5, 61.3, 60.7, 66.6, 41.6, 54.1, 55.6, 54.2, 50.3, 52.2, 52.8,
               45.7, 45.7, 80.35, 46.7, 59.6, 45, 39.9, 46.2, 80.2, 54.2],
    "blood pressure": ["138/82", "163/80", "155/71", "127/73", "174/87", "150/122", "152/80", "139/89", "165/88", "165/97", "167/83", "118/77",
                       "155/82", "150/85", "161/93", "117/71", "157/96", "176/91", "153/80", "156/78", "125/73", "141/93", "139/69", "128/69",
                       "152/93", "124/81", "109/76", "111/79", "170/102", "124/70"],
    "abdominal circumference": [85, 83, 80, 81, 89, 89, 96, 86, 78, 84, 96, 96, 99, 71, 89, 78, 90, 85, 78, 82, 75, 93, 102, 81, 86, 84, 72, 82, 114, 86],
    "blood sugar": [113, 134, 96, 178, 350, 357, 98, 111, 95, 169, 126, 159, 163, 109, 108, 111, 100, 145, 196, 107, 103, 109, 96, 188, 141, 87, 89, 94, 175, 121]
}

df = pd.DataFrame(data)

# Title
st.title("📊 Posyandu RW18 Health Data")

# Display data
st.subheader("📋 Raw Data")
st.dataframe(df)

# Summary statistics
st.subheader("📈 Summary Statistics")

numerical_cols = ["age", "height", "weight", "abdominal circumference", "blood sugar"]

stats = pd.DataFrame({
    "Mean": df[numerical_cols].mean(),
    "Median": df[numerical_cols].median(),
    "Mode": df[numerical_cols].mode().iloc[0]
})

st.dataframe(stats)

# Optional: Blood pressure breakdown
st.subheader("🩺 Blood Pressure Breakdown")
bp_split = df["blood pressure"].str.split("/", expand=True).astype(int)
bp_split.columns = ["Systolic", "Diastolic"]
df_bp = pd.concat([df[["no"]], bp_split], axis=1)
st.dataframe(df_bp)

# Optional: Visualizations
st.subheader("📊 Visualizations")

chart_option = st.selectbox("Choose a variable to visualize", numerical_cols)

st.bar_chart(df[chart_option])

