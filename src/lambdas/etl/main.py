from services.etl import ETLService
from fastapi import HTTPException
import json
import asyncio
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

loop = asyncio.get_event_loop()


session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("SESSION_TOKEN"),
    region_name="us-east-1"
)

lambda_client = session.client('lambda')

async def handler_etl(event, context):
    try:
        if (event):
            file_s3 = event["Records"][0]["s3"]["object"]["key"]
            print('Arquivo recebido:', file_s3)
            response = await ETLService.run(file=file_s3)
            print('Enviando arquivo para o lambda de predição:', response[0])
            lambda_client.invoke(
                FunctionName='arn:aws:lambda:us-east-1:425484609756:function:lambda-prediction',
                InvocationType='Event',
                Payload=json.dumps(response)
            )
            return 200, response
        else:
            return 400, "No file received!"

    except Exception as e:
        return 400, str(e)
    

def lambda_handler(event, context):
    result = loop.run_until_complete(handler_etl(event, context))
    # Create a response
    response = {
        "statusCode": result[0],
        "body": json.dumps({"message": result[1]})
    }
    print(response)
    return response
