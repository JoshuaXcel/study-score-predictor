#Importing Libraries
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the saved model and dataset
model = joblib.load("study_model.pkl")
df = pd.read_csv("data2-reg.csv")

#App title and description
st.title("📚 Study Hours vs Score Predictor")
st.write("Drag to select the number of hours studied to predict the exam score.")

#User input
hours = st.slider("Hours Studied", min_value=1.0, max_value=10.0, step=0.5)

#Prediction
predicted_score = model.predict([[hours]])[0]
st.metric(label="Predicted Score", value=f"{predicted_score:.1f}")

#Plotting original data + prediction line
st.subheader("Study Hours vs Score Chart")
fig, ax = plt.subplots()

#Original data points
ax.scatter(df["HoursStudied"], df["Score"], label="Original Data", alpha=0.7)

#Predicted regression line
new_hours = np.arange(1, 11, 0.5).reshape(-1, 1)
predicted_line = model.predict(new_hours)
ax.plot(new_hours, predicted_line, color="green", linestyle="--", label="Predicted Line")

#Marking the user's prediction
ax.scatter([hours], [predicted_score], color="red", zorder=5, label=f"Your Prediction ({hours}hrs)")

#Chart labels and legend
ax.set_xlabel("Study Hours")
ax.set_ylabel("Score")
ax.set_title("Study Hours vs Student Scores")
ax.legend()

st.pyplot(fig)