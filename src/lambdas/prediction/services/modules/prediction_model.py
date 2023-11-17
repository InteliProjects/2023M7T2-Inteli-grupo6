import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import HTTPException

class PredictionModel():
    async def predict(data):
        try:
            model = load_model("model")
            data = pd.DataFrame([data])
            prediction = predict_model(model, data=data)
            result_prediction = prediction["prediction_label"].iloc[0]
            return result_prediction
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))
