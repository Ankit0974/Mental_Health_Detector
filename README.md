# 🧠 Mental Health Risk Detection using BERT

## 📌 Overview

This project focuses on detecting mental health risk from textual data using a fine-tuned BERT model. The system analyzes user input and predicts the likelihood of mental health risk, enabling early identification and intervention.

---

## 🚀 Features

* 🔍 Text-based mental health risk prediction
* 🤖 Fine-tuned BERT model for classification
* ⚡ FastAPI backend for inference
* 🖥️ Streamlit frontend for user interaction
* 🐳 Dockerized architecture for deployment
* ☁️ Model hosted on Hugging Face Hub

---

## 🏗️ Project Architecture

User Input → Streamlit UI → FastAPI Backend → BERT Model → Prediction Output

---

## 🧠 Model Details

* Model: BERT (bert-base-uncased)
* Fine-tuned for binary classification (risk / no-risk)
* Dataset: Suicide Detection Dataset
* Frameworks: PyTorch, Transformers

---

## 📊 Performance Metrics

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 97.65% |
| Precision | 97.30% |
| Recall    | 98.01% |
| F1 Score  | 97.60% |

---

## ⚙️ Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* FastAPI
* Streamlit
* Docker

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Mental_Health_Detector.git
cd Mental_Health_Detector
pip install -r requirements.txt
```

---



## ▶️ Running the Project (Docker + ngrok)

### Step 1: Start the application using Docker

```bash
docker compose up --build
```

This will:

* Start the FastAPI backend on port `8000`
* Start the Streamlit frontend on port `8501`

---

### Step 2: Expose the frontend using ngrok

```bash
ngrok http 8501
```

This generates a public URL that can be shared to access the application.

---

### Step 3: Access the application

* Local: http://localhost:8501
* Public: (ngrok URL)

---

### ⚠️ Notes

* Ensure Docker is running before executing the command
* ngrok is required for external access (especially behind NAT/firewall)
* First run may take longer due to model loading

---



## ☁️ Model Hosting

The trained model is hosted on Hugging Face:

👉 https://huggingface.co/ankitml01/mental-health-model

---

## ⚠️ Challenges Faced

* Handling large model size (~400MB) during deployment
* Memory limitations on free cloud platforms
* Docker build context and dependency management
* Optimizing inference performance

---

## 🔮 Future Improvements

* Use lighter models (DistilBERT) for faster inference
* Add real-time API scaling
* Improve UI/UX
* Add multi-class classification
* Integrate with mobile or web apps

---

## 📌 Conclusion

This project demonstrates the end-to-end pipeline of building, training, and deploying an NLP-based machine learning system using modern tools and frameworks.

---

## 👨‍💻 Author

Ankit Roy
B.Tech CSE (AI & DS)
