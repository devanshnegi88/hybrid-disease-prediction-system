# 🩺 Hybrid Disease Prediction System

### Machine Learning–Powered Healthcare Decision Support

> A web-based machine learning application that analyzes user symptoms, predicts potential diseases, and recommends relevant hospitals for further professional consultation.

<p align="center">

**🌐 Live Demo:**  
<a href="https://hybrid-disease-prediction-system-2.onrender.com">https://hybrid-disease-prediction-system-2.onrender.com
</a>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Bootstrap-UI-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>

</p>

---

## ✨ What is Hybrid Disease Prediction System?

**Hybrid Disease Prediction System** is an end-to-end machine learning web application designed to provide users with a preliminary assessment based on their reported symptoms.

The application takes symptom inputs, processes them through a trained machine learning model, generates a predicted disease, and provides relevant hospital recommendations for further medical consultation.

The project combines:

**Machine Learning + Backend Engineering + Web Development + Healthcare Decision Support**

### Core Flow

```text
User Symptoms
      ↓
Input Validation
      ↓
Feature Processing
      ↓
Machine Learning Model
      ↓
Disease Prediction
      ↓
Hospital Recommendation
      ↓
Interactive Results
```

---

## 🎯 Key Capabilities

<table>
<tr>
<td width="50%">

### 🔍 Disease Prediction

Analyzes user-provided symptoms using a trained machine learning model to generate a preliminary disease prediction.

</td>

<td width="50%">

### 🏥 Hospital Recommendation

Maps predicted conditions to relevant hospitals for further professional medical consultation.

</td>
</tr>

<tr>
<td width="50%">

### ⚡ Fast Inference

Uses a lightweight Flask backend to process requests and perform model inference efficiently.

</td>

<td width="50%">

### 🛡️ Input Validation

Validates user input before passing data into the machine learning pipeline.

</td>
</tr>

<tr>
<td width="50%">

### 📱 Responsive Interface

Built with HTML, CSS, JavaScript, and Bootstrap for a responsive user experience.

</td>

<td width="50%">

### ☁️ Cloud Deployment

Deployed as a publicly accessible web application using Render.

</td>
</tr>
</table>

---

## 🧠 How It Works

### 01 — Symptom Collection

The user selects or enters the symptoms they are experiencing through the web interface.

### 02 — Input Processing

The backend validates the submitted data and converts the symptoms into the feature representation expected by the trained model.

### 03 — Machine Learning Inference

The processed features are passed to the trained machine learning model.

### 04 — Disease Prediction

The model generates a predicted disease based on the provided symptom pattern.

### 05 — Hospital Recommendation

The predicted condition is mapped to relevant hospitals that the user can consider for further consultation.

### 06 — Result Presentation

The prediction and recommendations are returned to the frontend and presented through the application interface.

---

# 🏗️ System Architecture

```text
                         ┌────────────────────┐
                         │       USER         │
                         │     Symptoms       │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │    Web Interface   │
                         │ HTML / CSS / JS    │
                         │    Bootstrap       │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Flask Backend    │
                         │ Request Handling   │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Input Validation & │
                         │   Preprocessing    │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │  ML Model          │
                         │  Inference         │
                         └─────────┬──────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │ Disease          │          │ Hospital         │
          │ Prediction       │          │ Recommendation   │
          └────────┬─────────┘          └────────┬─────────┘
                   │                             │
                   └──────────────┬──────────────┘
                                  ▼
                         ┌────────────────────┐
                         │   Results Page     │
                         └────────────────────┘
```

---

# 🛠️ Technology Stack

### Backend

| Technology | Role |
|---|---|
| **Python** | Core application and ML development |
| **Flask** | Web backend and request handling |

### Machine Learning

| Technology | Role |
|---|---|
| **Scikit-learn** | Model development and inference |
| **Pandas** | Dataset processing |
| **NumPy** | Numerical computation |

### Frontend

| Technology | Role |
|---|---|
| **HTML5** | Application structure |
| **CSS3** | Styling |
| **JavaScript** | Client-side functionality |
| **Bootstrap** | Responsive UI |

### Deployment

| Platform | Purpose |
|---|---|
| **Render** | Cloud deployment |

---

# 📂 Project Structure

```text
hybrid-disease-prediction-system/
│
├── data/
│   └── dataset.*
│
├── models/
│   └── trained_model.*
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── ...
│
├── app.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The structure above should be aligned with the actual repository before publishing.

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

- Python 3.x
- pip
- Git

## Clone the Repository

```bash
git clone https://github.com/devanshnegi88/hybrid-disease-prediction-system.git

cd hybrid-disease-prediction-system
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

# 🌐 Live Demo

### Try the Application

**  https://hybrid-disease-prediction-system-2.onrender.com**

> The application is deployed on Render and can be accessed directly through the live URL.

---

# 📊 Machine Learning Pipeline

```text
              Dataset
                 │
                 ▼
          Data Cleaning
                 │
                 ▼
       Feature Preparation
                 │
                 ▼
         Feature Encoding
                 │
                 ▼
         Model Training
                 │
                 ▼
        Model Evaluation
                 │
                 ▼
          Trained Model
                 │
                 ▼
       Flask Integration
                 │
                 ▼
        Real-Time Inference
```

The machine learning component is integrated directly into the application backend, allowing the trained model to be used for inference from incoming user requests.

---

# 🔮 Roadmap

The system can be extended with additional AI and healthcare capabilities.

### 🤖 Advanced AI

- [ ] Ensemble machine learning models
- [ ] Deep learning-based prediction
- [ ] Explainable AI using SHAP/LIME
- [ ] Prediction confidence and probability scores

### 🖼️ Medical Image Analysis

- [ ] CNN-based medical image classification
- [ ] X-ray analysis
- [ ] Image preprocessing pipeline

### 📄 Medical Document Intelligence

- [ ] OCR-based medical report extraction
- [ ] Automated report summarization
- [ ] Structured medical information extraction

### 🏥 Recommendation Engine

- [ ] Location-based hospital search
- [ ] Hospital specialization filtering
- [ ] Facility-based recommendations
- [ ] Distance-based ranking

### 🔐 Platform Improvements

- [ ] User authentication
- [ ] Prediction history
- [ ] Secure data storage
- [ ] API authentication
- [ ] Production monitoring and logging

---

# ⚠️ Limitations

This project is a **machine learning demonstration and healthcare decision-support system**, not a clinical diagnostic system.

The quality of predictions depends on:

- Training dataset quality
- Dataset coverage
- Feature representation
- Model performance
- Accuracy of user-provided symptoms

Symptoms alone may not provide sufficient information for a clinical diagnosis.

The application should therefore **not be used as a replacement for a qualified healthcare professional, diagnostic testing, or medical consultation.**

---

# 🔐 Privacy & Security Considerations

A production healthcare system would require significantly stronger privacy and security controls, including:

- Secure authentication
- Authorization
- Encryption
- Secure data storage
- Audit logging
- Data retention policies
- Healthcare privacy compliance

These considerations are important before using such a system with real patient information.

---

# 💡 Project Highlights

```text
✓ End-to-end ML application
✓ Symptom-based disease prediction
✓ Flask-powered backend
✓ Machine learning inference pipeline
✓ Hospital recommendation workflow
✓ Responsive web interface
✓ Input validation & error handling
✓ Cloud deployment
✓ Extensible architecture
```

---

# 👨‍💻 Author

## Devansh Negi

Backend Developer | Machine Learning Enthusiast

<p>
<a href="https://github.com/devanshnegi88">
<img src="https://img.shields.io/badge/GitHub-devanshnegi88-181717?style=for-the-badge&logo=github"/>
</a>

<a href="https://linkedin.com/in/devansh-negi005">
<img src="https://img.shields.io/badge/LinkedIn-Devansh%20Negi-0A66C2?style=for-the-badge&logo=linkedin"/>
</a>
</p>

---

## ⚕️ Medical Disclaimer

> **For educational purposes only.**
>
> This application provides machine learning–generated predictions and should not be interpreted as professional medical advice or diagnosis. Always consult a qualified healthcare professional for medical decisions.
