# 📚 Study Hours vs Score Predictor

![Python](https://img.shields.io/badge/Python-1E3A8A?logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-2563EB?logo=scikitlearn&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-1E40AF?logo=streamlit&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-1D4ED8?logo=pandas&logoColor=white)

A Streamlit web app that predicts a student's exam score from the number of hours they studied, using a Linear Regression model trained with scikit-learn.

## What it does

- Drag a slider to pick the hours studied (1 to 10 hours, in 0.5-hour steps)
- The app shows the **predicted score** straight away
- A chart plots the original data points, the model's regression line, and your prediction as a red point

## Dataset

`data2-reg.csv` is a small dataset of 19 rows with two columns:

| Column | Meaning |
|---|---|
| `HoursStudied` | Hours studied (1 to 10) |
| `Score` | Exam score |

## Model

- **Algorithm:** scikit-learn `LinearRegression`, with one feature (`HoursStudied`) predicting `Score`
- **Saved model:** `study_model.pkl`, loaded with `joblib`

## How to run

```bash
git clone https://github.com/JoshuaXcel/study-score-predictor.git
cd study-score-predictor
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually http://localhost:8501).

## Project structure

```
app.py             Streamlit app: slider, prediction and chart
data2-reg.csv      Training data (hours studied vs score)
study_model.pkl    Trained Linear Regression model
requirements.txt   Python dependencies
```

## Tech used

Python · scikit-learn · Streamlit · pandas · NumPy · Matplotlib · joblib

## Author

**Joshua Mudana (Excel)**, AI & Machine Learning Engineer

[Portfolio](https://joshuaxcel.github.io/joshuamudana-portfolio/) · [GitHub](https://github.com/JoshuaXcel) · [X](https://x.com/JoshuaXcell) · mudanajoshua@gmail.com
