import pandas as pd
from fastapi import HTTPException
import pyarrow


class Extract():
    @staticmethod
    def extract_parquet(file:str):
        try:
            file = "https://bucket-azul-files.s3.amazonaws.com/"+file
            dataframe = pd.read_parquet(file, engine='auto')
            return dataframe
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))