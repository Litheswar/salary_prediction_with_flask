import pickle 
import numpy as np
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "models", "model.pkl")
model_path = os.path.abspath(model_path)

with open(model_path, "rb") as f:
    model = pickle.load(f)

logging.info("Model loaded successfully")

def predict_salary(experience):
    logging.info(f"Model received: {experience}")

    result = model.predict(np.array([[experience]]))

    logging.info(f"Model result: {result[0]}")

    return result[0]
