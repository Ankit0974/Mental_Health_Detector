
# 🧠 Mental Health Risk Detection using BERT

## 📌 Overview

This project focuses on detecting mental health risk from textual data using a fine-tuned BERT model. The system analyzes user input and predicts the likelihood of mental health risk, enabling early identification and intervention.

---
## 🌐 Frontend (Live Demo)

https://mental-health-frontend-latest.onrender.com/

## ⚙️ Backend API

https://mental-health-risk-backend-production.up.railway.app/docs

# ⚠️ Important Note

This project uses **Railway's free tier** for backend deployment.

If the backend API does not respond or the frontend shows connection errors, it is likely because the Railway monthly credits have been exhausted.

In that case:

- The frontend may still load successfully.
- Predictions will not work until the backend service is restarted after credits reset or the deployment is upgraded.

This is a deployment limitation, **not an issue with the application itself**.

---
## 📸 Screenshots & Demo

- Screenshots are available in the **Screenshots/** directory.
- A complete walkthrough video is available in the **Demo/** directory.

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
* Dataset: Suicide Detection Dataset(https://drive.google.com/file/d/1EUw3V9ul41rh6lb2jJegoP8NecK6xSy3/view?usp=sharing)
* Frameworks: PyTorch, Transformers

---

## 🚀 Model Improvements

The model was iteratively improved through multiple rounds of testing and retraining.

Key improvements include:

- Fine-tuned BERT for binary mental health risk classification.
- Identified false positives through manual testing on real-world conversations.
- Added additional non-risk examples including:
  - Greetings
  - Family conversations
  - Daily-life activities
  - Education
  - Programming
  - Sports
  - Casual conversations
- Retrained the model on the augmented dataset to improve generalization.
- Hosted the final model on Hugging Face for lightweight deployment.

## 📊 Performance Metrics

| Metric | Score |
|---------|-------|
| **Accuracy** | **97.00%** |
| **Precision** | **97.00%** |
| **Recall** | **97.00%** |
| **F1 Score** | **97.00%** |
| **ROC-AUC Score** | **0.9955** |

## ⚙️ Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* FastAPI
* Streamlit
* Docker

---

## 🐳 Docker Images
Frontend Image :- https://hub.docker.com/repository/docker/ankitroy01/mental-health-frontend/general
Backend Image :- https://hub.docker.com/repository/docker/ankitroy01/mental-health-risk-backend/general


## ☁️ Model Hosting

The trained model is hosted on Hugging Face:

👉 https://huggingface.co/ankitml01/mental-health-model

---

# ⚠️ Challenges Faced

Building a reliable mental health risk detector involved several practical and machine learning challenges:

- **False positives on everyday conversations:**  
  The initial BERT model incorrectly classified simple phrases such as *"I love my family"*, *"Hello"*, *"Good morning"*, and other daily conversations as mental health risk due to biases in the training dataset.

- **Dataset bias:**  
  The original dataset contained relatively few examples of neutral, positive, and everyday conversations, causing the model to over-predict the risk class for ordinary text.

- **Data augmentation:**  
  To improve generalization, additional non-risk examples containing greetings, family-related sentences, daily conversations, hobbies, work, education, and casual discussions were created and merged with the original dataset before retraining.

- **Improving real-world robustness:**  
  The model was tested on numerous unseen real-world examples rather than relying only on benchmark metrics, helping identify prediction errors that standard evaluation metrics did not reveal.

- **Large model deployment:**  
  Deploying a BERT model (~400 MB) on free cloud platforms required careful optimization because of memory and storage limitations.

- **Docker build configuration:**  
  Managing Docker build contexts, image size, and dependency installation required multiple iterations to ensure successful containerization.

- **Cloud deployment limitations:**  
  Free-tier hosting services such as Railway have monthly credit limits, which can temporarily make the backend unavailable after the credits are exhausted.

- **Model hosting:**  
  Instead of packaging the large model inside the Docker image, the trained model was hosted on Hugging Face Hub and downloaded dynamically during backend startup, reducing image size and simplifying deployment.

---



---

## 📌 Conclusion

This project demonstrates the end-to-end pipeline of building, training, and deploying an NLP-based machine learning system using modern tools and frameworks.

---

## 👨‍💻 Author

Ankit Roy
B.Tech CSE (AI & DS)
