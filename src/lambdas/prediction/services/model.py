from fastapi import HTTPException
from .modules.prediction_infos import PredictionInfos
from .modules.prediction_model import PredictionModel

class ModelService:

    async def run(flightFileId: str):
        try:
            print("Colentando dados:", flightFileId)
            result = await PredictionInfos.load(flightFileId)

            print("Fazendo predição: ", result)
            prediction = await PredictionModel.predict(result)

            print("Salvando predição: ", prediction)
            await PredictionInfos.update(flightFileId, prediction)

            print("Predição: ", prediction)
            return prediction
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))
