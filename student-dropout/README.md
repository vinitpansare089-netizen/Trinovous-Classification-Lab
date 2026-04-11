# 🎓 Student Dropout Prediction (Trinovous Project 2)

## 🚀 Overview

This project is part of my **Trinovous AI/ML journey**, focusing on building a real-world **classification system** from scratch using an industry-style modular pipeline.

The goal is to predict whether a student is likely to **drop out** or **continue**, enabling early intervention strategies.

---

## 🎯 Problem Statement

Educational institutions face high dropout rates.
This project builds a machine learning model to predict:

* ❌ Dropout (1)
* ✅ Not Dropout (0)

---

## 🧠 Key Learning Objectives

* Understand classification deeply 
* Build modular ML pipelines (industry-level structure)
* Handle data leakage and feature selection
* Learn evaluation metrics beyond accuracy:

  * Precision
  * Recall
  * F1-score
  * Confusion Matrix

---

## 📂 Project Structure

```
student_dropout_project/
│
├── data/
│   ├── dataset.csv
│   └── processed_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── evaluate.py
│
├── pipeline/
│   └── train_pipeline.py
│
├── models/
│   └── saved_model.pkl
│
├── notebooks/
│
└── README.md
```

---

## ⚙️ Pipeline Flow

```
Raw Data → Cleaning → Target Creation → Feature Selection → Processed Data → Model Training → Evaluation
```

---

## 📊 Dataset

Dataset used:
**Student Dropout and Academic Success Dataset (Kaggle)**

Key features include:

* Academic performance (1st semester)
* Demographics
* Financial status
* Enrollment details

---

## 🧹 Data Preprocessing

* Cleaned column names
* Converted multi-class target → binary classification
* Removed data leakage (2nd semester features)
* Dropped unnecessary columns

---

## 🤖 Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🔥 Key Insights

* Academic performance is a strong predictor of dropout
* Financial factors (debtor, tuition status) impact risk
* Early semester data is sufficient for prediction

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn

---

## 🚀 Future Improvements

* Hyperparameter tuning
* Feature importance visualization
* FastAPI deployment
* Full-stack integration (Node.js + React)

---

## 🧠 Author

**Vinit (Trinovous)**
Building AI systems with depth, not shortcuts.

---

## ⭐ Note

This project focuses on **understanding + implementation**, not just results.
Every step is designed to build strong ML intuition.

---
