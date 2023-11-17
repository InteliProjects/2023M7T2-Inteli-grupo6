from pydantic import BaseModel


class OutputModel(BaseModel):
    prediction: float