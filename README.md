# PyTech Arena 2026 – Level 2 Submission

## 👩‍💻 Team Details
**Team Name:** Codepy  
**Course:** B.Tech – Artificial Intelligence & Machine Learning  
**College:** Avanthi Institute of Engineering & Technology  

---

## 📌 Selected Problems

## 1️⃣ Problem 7 – Pass/Fail Predictor (Classification)

### 📖 Description
This project predicts whether a student will **Pass or Fail** based on academic performance using a Machine Learning classification model.

### ⚙️ Implementation Details
- Created a target column:
  - Pass if average score ≥ 40
  - Fail otherwise
- Used 80% training and 20% testing split
- Trained a Logistic Regression model
- Displayed:
  - Training and testing sample size
  - Confusion Matrix
  - Accuracy Score
- Implemented interactive prediction using user input
- Modular structure using OOP (`main.py` + `model.py`)

### 📊 Dataset Source
Student Performance Dataset (Kaggle):  
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

### ▶️ How to Run
cd Pass_Fail_Predictor

python main.py


---

## 2️⃣ Problem 8 – House Price Prediction (Regression)

### 📖 Description
This project predicts house prices using a Linear Regression model trained on the KC House Price dataset.

### ⚙️ Implementation Details
- Selected feature columns:
  - sqft_living
  - bedrooms
  - bathrooms
- Used 80% training and 20% testing split
- Trained Linear Regression model
- Displayed R² score
- Implemented interactive price prediction
- Price displayed in:
  - USD
  - INR (Lakhs / Crores automatically formatted)
- Clean modular structure using OOP (`main.py` + `model.py`)

### 📊 Dataset Source
KC House Price Dataset (Kaggle):  
https://www.kaggle.com/datasets/shivachandel/kc-house-data

### ▶️ How to Run

cd House_Price_Prediction

python main.py


---

## 📦 Libraries Used
- pandas
- scikit-learn

---

## 🏗 Project Structure

PyTech-Level2-Codepy/
│
├── House_Price_Prediction/
│ ├── main.py
│ ├── model.py
│ ├── kc_house_data.csv
│ └── requirements.txt
│
├── Pass_Fail_Predictor/
│ ├── main.py
│ ├── model.py
│ ├── students.csv
│ └── requirements.txt
│
├── README.md
└── .gitignore

