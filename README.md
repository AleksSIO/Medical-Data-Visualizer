# Medical Data Visualizer

This is the solution to the **Medical Data Visualizer** project from the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification.

## 🩺 Project Overview

The goal of this project is to analyze and visualize data from medical examinations. Using **Pandas**, **Matplotlib**, and **Seaborn**, we generate visualizations to explore relationships between **cardiovascular disease** and various health/lifestyle factors.

---

## 📊 Dataset

- File: `medical_examination.csv`
- Each row represents a patient
- Columns include: `age`, `height`, `weight`, `ap_hi`, `ap_lo`, `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `cardio`

---

## 📌 Tasks Completed

1. **Import Data** using Pandas from `medical_examination.csv`
2. **Add an `overweight` column** (based on BMI > 25 → 1, else 0)
3. **Normalize data**:
   - `cholesterol` and `gluc`: 0 = normal, 1 = above normal or worse
4. **Categorical Plot**:
   - Melt data using `pd.melt`
   - Group data by feature, value, and cardio
   - Plot using `sns.catplot()`
5. **Heat Map**:
   - Clean invalid entries (e.g., `ap_lo > ap_hi`, extreme height/weight)
   - Compute correlation matrix
   - Plot using `sns.heatmap()` with upper-triangle mask

---

## 📁 File Structure

├── medical_data_visualizer.py # Main analysis and plotting functions 
├── medical_examination.csv # Provided dataset 
├── test_module.py # Unit tests for project validation 
├── main.py # Development/test runner 
