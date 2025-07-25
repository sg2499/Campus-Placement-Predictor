# 🎓 Campus Placement Predictor using Flask & Machine Learning

![GitHub repo size](https://img.shields.io/github/repo-size/sg2499/Campus-Placement-Predictor)
![GitHub stars](https://img.shields.io/github/stars/sg2499/Campus-Placement-Predictor?style=social)
![Last Commit](https://img.shields.io/github/last-commit/sg2499/Campus-Placement-Predictor)
![Built with Flask](https://img.shields.io/badge/Built%20With-Flask-blue)

This repository hosts a **Campus Placement Predictor** built with **Streamlit**, **Pandas**, and **Scikit-learn**. It predicts whether a student is likely to be placed based on academic and profile parameters. The project also includes a **Jupyter Notebook** that explains data preprocessing, EDA, model training, and evaluation.

---

## 📁 Project Structure

```
📦Campus-Placement-Predictor/
├── new-app.py                            # Streamlit web app
├── CPP.pkl                               # Trained Random Forest model
├── Placement_Data_Full_Class.csv         # Dataset used for training
├── Campus Placement Predictor.ipynb      # Notebook with full ML pipeline
├── requirements.txt                      # Python dependencies
├── CPP App.png                           # Screenshot of the UI
└── README.md                             # Project documentation
```

---

## 🚀 Features

- 🎯 Predicts whether a student will be placed based on:
  - Gender
  - Specialization
  - Work Experience
  - SSC, HSC, Degree %, MBA %
- 📊 Displays probability of placement
- 🧠 Random Forest Classifier trained on real-world campus data
- 🌐 Fully deployed on local Flask server

---

## 📊 Dataset Description

- **Source:** Supplied dataset (`Placement_Data_Full_Class.csv`)
- **Size:** 215 rows × 15 columns
- **Features used:**
  - Gender (binary)
  - Stream/Specialization (binary)
  - Work Experience (binary)
  - SSC %, HSC %, Degree %, MBA %
- **Target:** Placement status (Placed / Not Placed)

---

## 🧠 ML Model Details

- **Model:** Random Forest Classifier
- **Libraries Used:** Scikit-learn, Pandas, NumPy, Seaborn
- **Evaluation Metrics:** Accuracy, Confusion Matrix, ROC Curve
- **Best Accuracy Achieved:** 87.5%

---

## 💻 How to Run the App Locally

### 🔧 Clone the Repository

```bash
git clone https://github.com/sg2499/Campus-Placement-Predictor.git
cd Campus-Placement-Predictor
```

### 🐍 Set up a Virtual Environment

```bash
conda create -n cpp_env python=3.11
conda activate cpp_env
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the Streamlit App

```bash
streamlit run new_app.py
```

App will run locally at:  
📍 `http://127.0.0.1:5000`

---

## 📸 UI Screenshot

<img src="CPP App.png" width="100%" alt="Campus Placement Prediction Form UI"/>

---

## 📄 Sample Input

| Gender | Spec | Tech | Work | SSC | HSC | Degree | MBA |
|--------|------|------|------|-----|-----|--------|-----|
| 1      | 0    | 1    | 1    | 78.6| 70.5| 72.1   | 65.3|

**Output:** ✅ *Will be Placed* with 82.4% probability

---

## 🧪 Dependencies

```txt
streamlit
numpy>=1.9.2
pandas>=0.19
scikit-learn>=0.18
```

> 📦 Full list in [`requirements.txt`](requirements.txt)

---

## 🌐 Live Demo
You're welcome to explore the app by visiting the link provided below.

👉 [Try Yourself](https://campus-placement-predictor-ktf7emqi8b6xzqbcezytzc.streamlit.app/)

---

## ✍️ Author

Created with ❤️ by **Shailesh Gupta**  
🔗 GitHub: [sg2499](https://github.com/sg2499)  
📩 Email: shaileshgupta841@gmail.com

---

> Empowering students with the right tools for career prediction 🌟
