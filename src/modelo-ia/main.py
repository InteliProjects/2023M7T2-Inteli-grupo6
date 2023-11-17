import pandas as pd
from model.inputModel import InputModel
from model.outputModel import OutputModel
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
from typing import Any

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("model")

async def hendler(event: dict, context: Any) -> dict:
    print(event)
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


