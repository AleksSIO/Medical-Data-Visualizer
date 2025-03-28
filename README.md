# 🩺 Medical Data Visualizer

This project is part of the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification.  
It visualizes patient health data to explore trends and correlations between **lifestyle choices**, **body measurements**, and **cardiovascular disease**.

---

## 📁 Project Structure

```
medical_data_visualizer.py   # Script with analysis and plotting logic  
main.py                      # Development entrypoint to test your function  
test_module.py               # Unit tests for validation  
medical_examination.csv      # Provided medical dataset  
catplot.png                  # Categorical plot output  
heatmap.png                  # Correlation heatmap output  
```

---

## 📊 Features

- Loads a real-world medical dataset with 13 features per patient  
- Adds a new column to classify patients as **overweight** based on BMI  
- Normalizes some values (e.g., cholesterol and glucose levels)  
- Generates two main visualizations:
  - **Categorical plot** (bar chart) to compare health indicators vs. cardiovascular disease
  - **Correlation heatmap** to explore relationships between all numerical features

---

## 🧪 Technologies Used

- **Python 3**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 🚀 How to Run the Project

1. Install required libraries:

```bash
pip install pandas matplotlib seaborn
```

2. Run the project:

```bash
python main.py
```

This will:

- Generate and save two plots: `catplot.png` and `heatmap.png`  
- Run tests from `test_module.py` to validate your solution

---

## 📈 Output Plot Descriptions

### 📌 catplot.png

A bar chart showing counts of patients grouped by:
- Lifestyle choices (e.g., smoke, alcohol, active)
- Health levels (cholesterol, glucose, overweight)
- Presence or absence of **cardiovascular disease**

### 📌 heatmap.png

A correlation matrix showing how variables like:
- Blood pressure
- BMI
- Age
- Cholesterol

...are related to each other, visualized with a heatmap.

---

## 📚 Dataset Source

> Medical Examination Data  
> Provided by freeCodeCamp  
> Based on synthetic or anonymized data for educational use

