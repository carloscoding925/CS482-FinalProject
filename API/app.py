# Carlos Hernandez & Jonathan Nunez

from fastapi import FastAPI
from pydantic import BaseModel
from models.Logistic_Regression import MyLogisticRegression

app = FastAPI()

dataset_path = "/data/weather_classification_data.csv"
logistic_model = MyLogisticRegression(dataset_path)
logistic_model.model_predict_logistic()

# Sample endpoint to test in remix app
@app.get("/hello")
def read_root():
    return {"Hello": "World"}

# Sample async function
@app.get("/sample")
async def read_item():
    return {"Hello": "Sample"}

class Features(BaseModel):
    features: str

@app.post("/predict")
def predict(features: Features):
    try:
        features_list = [float(x) for x in features.features.split(',')]
        result = predict_from_features(logistic_model, features_list)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid input format")