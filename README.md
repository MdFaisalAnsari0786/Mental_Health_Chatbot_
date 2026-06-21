# Mental Health Companion Chatbot

## Project Overview

Mental Health Companion Chatbot is an AI-powered application designed to support students dealing with stress, anxiety, loneliness, and emotional challenges. The chatbot uses Machine Learning and Natural Language Processing (NLP) to detect user sentiment and provide empathetic responses, motivational messages, and relaxation tips.

## Problem Statement

Students often face academic pressure, stress, anxiety, and loneliness but may hesitate to seek professional counseling. This project provides a safe and accessible platform where students can express their feelings and receive supportive responses.

## Features

* Sentiment Analysis (Positive, Negative, Neutral)
* Empathetic AI Responses
* Relaxation and Wellness Tips
* User-Friendly Streamlit Interface
* Machine Learning-based Mood Detection
* NLP Text Processing

## Technology Stack

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NLTK
* Joblib

## Project Structure

Mental_Health_Chatbot/

├── data/

│   └── emotions.csv

├── models/

│   └── sentiment_model.pkl

├── src/

│   ├── preprocess.py

│   ├── train_model.py

│   ├── chatbot.py

│   └── tips.py

├── app.py

├── requirements.txt

└── README.md

## Installation

### Clone Repository

git clone <repository_url>

cd Mental_Health_Chatbot

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

## Training the Model

Navigate to the src folder:

cd src

Run:

python train_model.py

This creates:

models/sentiment_model.pkl

## Running the Application

Return to the project root folder:

cd ..

Run Streamlit:

streamlit run app.py

Open the browser:

http://localhost:8501

## Dataset

The dataset contains text samples labeled as:

* Positive
* Negative
* Neutral

The model learns to classify user messages into these sentiment categories.

## Future Enhancements

* Voice-Based Interaction
* Text-to-Speech Responses
* Mood Tracking Dashboard
* Emergency Helpline Integration
* Multilingual Support
* Deep Learning Models (BERT, LSTM)

## Author

Mohammad Faisal Ansari

Computer Science Engineering Student

## License

This project is developed for educational and research purposes.
