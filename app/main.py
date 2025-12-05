import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("./data/personnel_mock.csv")

df = load_data()

st.title("Squad Training & Personnel Tracker")
st.write("Mock system inspired by my experience leading an 8-member squad (ranked 1st out of 123 squads).")

st.subheader("📋 Personnel Overview")
st.dataframe(df)

st.subheader("🏋️ Training Evaluation (Mock)")
name = st.selectbox("Select Soldier", df["name"])
score = st.slider("Training Score", 0, 100, 80)

if st.button("Save (Mock)"):
    st.success(f"{name}'s score ({score}) is recorded (simulation only).")
