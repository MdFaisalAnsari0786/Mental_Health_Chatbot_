import os
import random
import joblib

from preprocess import clean_text
from tips import tips

# Absolute path to models folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")

model = joblib.load(MODEL_PATH)

def get_response(user_input):

    processed = clean_text(user_input)

    sentiment = model.predict([processed])[0]

    # Convert numeric predictions to labels
    label_map = {
        0: "negative",
        1: "neutral",
        2: "positive"
    }

    sentiment = label_map.get(sentiment, str(sentiment).lower())

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

    response = random.choice(
        responses.get(
            sentiment,
            ["Thank you for sharing your thoughts."]
        )
    )

    tip = random.choice(
        tips.get(
            sentiment,
            ["Take a short break and practice self-care."]
        )
    )

    return sentiment, response, tip