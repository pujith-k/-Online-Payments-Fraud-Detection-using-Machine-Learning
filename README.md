# Online Payments Fraud Detection with Machine Learning

> A premium, real-time web application that detects fraudulent online payment transactions using Machine Learning.

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange)

---

## 📸 Screenshots

### 1. Home Page / Transaction Analysis Form
*A modern, dark-themed UI with glassmorphism for entering transaction details.*
![Home Page](screenshots/home_page.png)

### 2. Fraud Prediction Result
*Real-time risk assessment and clear indicator when a transaction is flagged as fraudulent.*
![Prediction Result](screenshots/prediction_result.png)

---

## 📖 Project Overview

The introduction of online payment systems has revolutionized financial transactions, making them faster and easier. However, this has also led to a significant increase in payment fraud. This project addresses the challenge by providing a **Machine Learning-powered web application** that classifies online transactions as fraudulent or legitimate in real-time.

### Key Features
- **Real-Time Fraud Prediction**: Enter transaction details and receive instant fraud/no-fraud classification within milliseconds.
- **Trained Machine Learning Model**: Uses a Decision Tree Classifier trained on the PaySim synthetic financial dataset, achieving **97.6% accuracy**.
- **Premium User Interface**: Dark-themed UI with glassmorphism effects, dynamic CSS animations, and fully responsive design.
- **Comprehensive Analysis**: Supports 5 transaction types (Cash Out, Payment, Cash In, Transfer, Debit).

---

## 🛠️ Technologies Used

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python Flask | Web server and API routing |
| **Machine Learning** | Scikit-Learn | Decision Tree model training and inference |
| **Data Processing** | NumPy & Pandas | Data manipulation and analysis |
| **Frontend** | HTML5 / CSS3 / JavaScript | Responsive user interface with modern styling |
| **Model Persistence** | Pickle | Saving and loading the pre-trained ML model |

---

## 🗂️ Project Structure

The repository is organized into clearly defined folders for ease of use:

```text
📁 Document/
   ├── Project_Documentation.pdf    # Full documentation (architecture, EDA, API, etc.)
📁 Project Files/
   ├── app.py                       # Main Flask server
   ├── retrain_model.py             # Script to regenerate the trained model
   ├── main.ipynb                   # Jupyter notebook with EDA and training pipeline
   ├── static/                      # CSS styling, images, and model.pkl
   └── templates/                   # HTML templates (index.html)
📁 Video Demo/
   └── video demo.mov               # Video demonstration of the working application
📄 README.md                        # This file
📄 .gitignore                       # Git ignore rules
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/pujith-k/-Online-Payments-Fraud-Detection-using-Machine-Learning.git
cd -Online-Payments-Fraud-Detection-using-Machine-Learning
cd "Project Files"
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed. It is recommended to use a virtual environment.
```bash
pip install flask scikit-learn numpy pandas
```

### 3. Run the Flask Application
```bash
python3 app.py
```
The server will start on `http://127.0.0.1:5000/`. Open this link in your web browser.

---

## 📊 Dataset Information

This project is built using the [PaySim synthetic financial dataset](https://www.kaggle.com/ealaxi/paysim1) from Kaggle.
- **Total records:** 6,362,620 transactions.
- **Imbalance:** Highly imbalanced — only 0.13% of transactions are fraudulent.
- **Features Used:** `type`, `amount`, `oldbalanceOrg`, `newbalanceOrig`.

---

## 👥 Meet the Team

| Name | Role |
| :--- | :--- |
| **P Varshitha** | Team Leader |
| **G Lokanath Reddy** | Team Member |
| **K Pujith** | Team Member |
| **T Sruthi** | Team Member |

**College:** Annamacharya Institute of Technology & Sciences  
**Team ID:** LTVIP2026TMIDS41562
