from .modules.transform import Transform
from .modules.load import Load
from .modules.extract import Extract
from fastapi import HTTPException
import asyncio

class ETLService:
    @staticmethod
    async def run(file: str):
        try:
            print('Carregando arquivo:', file)
            dataframe = Extract.extract_parquet(file=file)
            print('Transformando arquivo:', file)
            dataframe = Transform.transform_parquet(dataframe=dataframe)
            print('Carregando dados no banco:', file)
            response = await Load.load_parquet(dataframe=dataframe, file=file)
            return response
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))
