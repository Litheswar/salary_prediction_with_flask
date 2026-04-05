from app.model_utils import predict_salary
import logging

def get_prediction(data):
    logging.info("Service Layer Started")
    
    if not data:
        raise ValueError("No data provided for prediction")
    
    if "experience" not in data:
        raise ValueError("Missing 'experience' in input data")
    
    experience = float(data.get('experience'))
    
    if experience < 0:
        raise ValueError("Experience cannot be negative")
    
    prediction = predict_salary(experience)
    logging.info("Service layer completed")

    return prediction
    