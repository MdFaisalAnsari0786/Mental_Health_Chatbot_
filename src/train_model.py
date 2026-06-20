import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from preprocess import clean_text

df = pd.read_csv("../data/emotions.csv")

df["text"] = df["text"].apply(clean_text)

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(df["text"], df["label"])

joblib.dump(model, "../models/sentiment_model.pkl")

print("Model trained successfully")