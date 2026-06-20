import random
import joblib

from preprocess import clean_text
from tips import tips

model = joblib.load("../models/sentiment_model.pkl")

def get_response(user_input):

    processed = clean_text(user_input)

    sentiment = model.predict([processed])[0]

    responses = {
        "positive": [
            "That's wonderful to hear.",
            "I'm happy you're feeling good.",
            "Keep believing in yourself."
        ],

        "neutral": [
            "Thank you for sharing.",
            "I understand.",
            "Let's focus on something positive today."
        ],

        "negative": [
            "I'm sorry you're feeling this way.",
            "Your feelings are valid.",
            "Remember that difficult moments pass."
        ]
    }

    response = random.choice(responses[sentiment])

    tip = random.choice(tips[sentiment])

    return sentiment, response, tip