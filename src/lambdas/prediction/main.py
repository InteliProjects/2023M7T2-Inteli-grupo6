from services.model import ModelService
from typing import Any
import json
import asyncio

loop = asyncio.get_event_loop()

async def hendler_prediction(event: dict, context: Any) -> dict:
    try:
        if event:
            print("Event recebido:", event)
            response = await ModelService.run(event)

            print("Predição Finalizada: ", response)
            return 200, "OK"
        else:
            return 400, "No file received!"

    except Exception as e:
        return 400, str(e)


def lambda_handler(event, context):
    result = loop.run_until_complete(hendler_prediction(event, context))
    # Create a response
    response = {
        "statusCode": result[0],
        "body": json.dumps({"message": result[1]})
    }
    print(response)
    return response


