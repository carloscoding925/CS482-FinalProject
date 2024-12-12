# Carlos Hernandez & Jonathan Nunez

import joblib
import torch
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.Logistic_Regression import MyLogisticRegression, predict_from_features
from models.Neural_Network import MultiLayerNet, preprocess_features, evaluate_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logistic_model = MyLogisticRegression()
metrics = logistic_model.model_predict_logistic()

class Features(BaseModel):
    features: str

@app.post("/predict/logistic_model")
def predict(features: Features):
    try:
        features_list = features.features.split(",")

        features_list = [
            float(features_list[0]),  # temperature
            float(features_list[1]),  # humidity
            float(features_list[2]),  # windSpeed
            float(features_list[3]),  # precipitation
            features_list[4],         # cloudCover
            float(features_list[5]),  # atmosphericPressure
            float(features_list[6]),  # uvIndex
            features_list[7],         # season
            float(features_list[8]),  # visibility
            features_list[9]          # location
        ]

        le_cloudCover = joblib.load('le_cloudCover.pkl')
        le_season = joblib.load('le_season.pkl')
        le_location = joblib.load('le_location.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoder = joblib.load('label_encoder.pkl')

        features_list[4] = le_cloudCover.transform([features_list[4]])[0]
        features_list[7] = le_season.transform([features_list[7]])[0]
        features_list[9] = le_location.transform([features_list[9]])[0]

        input_features = scaler.transform([features_list])

        result = predict_from_features(logistic_model.model_logistic, input_features, label_encoder)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid input format: " + str(e))
    
@app.post("/predict/neural_network")
def predict(features: Features):
    try:
        features_list = features.features.split(",")

        features_list = [
            float(features_list[0]),  # temperature
            float(features_list[1]),  # humidity
            float(features_list[2]),  # windSpeed
            float(features_list[3]),  # precipitation
            features_list[4],         # cloudCover
            float(features_list[5]),  # atmosphericPressure
            float(features_list[6]),  # uvIndex
            features_list[7],         # season
            float(features_list[8]),  # visibility
            features_list[9]          # location
        ]

        columns = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation', 'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season', 'Visibility', 'Location']
        input_df = pd.DataFrame([features_list], columns=columns)

        input_features = preprocess_features(features_list)

        input_size = input_features.shape[1]
        num_classes = len(joblib.load('nn_label_encoder.pkl').classes_)

        model = MultiLayerNet(input_size, num_classes)

        checkpoint = torch.load('mln.pth')
        model.load_state_dict(checkpoint['model_state_dict'])
        model.eval()

        input_tensor = torch.tensor(input_features, dtype=torch.float32)

        with torch.no_grad():
            predictions = model(input_tensor)
            prediction_class = torch.argmax(predictions, dim=1).item()

        label_encoder = joblib.load('nn_label_encoder.pkl')
        predicted_label = label_encoder.inverse_transform([prediction_class])[0]

        return {"Predicted Class": predicted_label}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid input format: " + str(e))

@app.post("/predict/decision_tree")
def predict():
    print()