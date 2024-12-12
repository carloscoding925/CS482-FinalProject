# Carlos Hernandez & Jonathan Nunez

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.Logistic_Regression import MyLogisticRegression, predict_from_features

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

        # Transform the categorical features
        features_list[4] = le_cloudCover.transform([features_list[4]])[0]
        features_list[7] = le_season.transform([features_list[7]])[0]
        features_list[9] = le_location.transform([features_list[9]])[0]

        input_features = scaler.transform([features_list])

        result = predict_from_features(logistic_model.model_logistic, input_features, label_encoder)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid input format")