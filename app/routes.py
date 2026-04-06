from flask import Blueprint, request, jsonify, render_template, make_response
from app.services.prediction_service import get_prediction
import logging
import os


routes = Blueprint('routes', __name__)
API_KEY = os.getenv("API_KEY")


@routes.route("/")
def home():
    return render_template("index.html")


@routes.route("/predict", methods=["POST"])
def predict():

    logging.info("Predict route hit")

    user_key = request.headers.get("x-api-key")

    if user_key != API_KEY:
        return make_response("fail", "Unauthorized"), 401

    data = request.get_json()

    prediction = get_prediction(data)

    return make_response("success", "Prediction successful", {
        "prediction": prediction
    })



def make_response(status, message, data=None):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })
