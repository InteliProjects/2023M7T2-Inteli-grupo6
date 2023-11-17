
from fastapi import HTTPException
from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os
load_dotenv()

class PredictionInfos():
    @staticmethod
    async def load(flightFileId:str):
        try:
            DB_USER = os.getenv("DB_USER")
            DB_PASSWORD = os.getenv("DB_PASSWORD")
            DB_HOST = os.getenv("DB_HOST")
            DB_PORT = os.getenv("DB_PORT")
            DB_NAME = os.getenv("DB_NAME")

            con = psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST, port= DB_PORT)

            cur = con.cursor()

            cur.execute('SELECT "aircraftSerNum1","amscChBasHealthStatus1", "amscChBasHealthStatus2","amscHprsovDrivF1","amscHprsovDrivF2","amscPrsovDrivF1","amscPrsovDrivF2","basBleedLowPressF1","basBleedLowPressF2","basBleedLowTempF1","basBleedLowTempF2","basBleedOverPressF1","basBleedOverPressF2","basBleedOverTempF1","basBleedOverTempF2","bleedAcsBleedConfigStatus1","bleedAcsBleedConfigStatus2","bleedFavTmCmd1","bleedFavTmCmd2","bleedFavTmFbk1","bleedFavTmFbk2","bleedHprsovCmdStatus1","bleedHprsovCmdStatus2","bleedHprsovOpPosStatus1","bleedHprsovOpPosStatus2","bleedMonPress1","bleedMonPress2","bleedOnStatus1","bleedOnStatus2","bleedOutTemp1","bleedOutTemp2","bleedOutTempTarget1","bleedOutTempTarget2","bleedOverpressCas1","bleedOverpressCas2","bleedPrecoolDiffPress1","bleedPrecoolDiffPress2","bleedPrsovClPosStatus1","bleedPrsovClPosStatus2","bleedPrsovFbk1","bleedPrsovFbk2","bleedPrsovOpPosStatus1","bleedPrsovOpPosStatus2","bleedPrsovTmCmd1","bleedPrsovTmCmd2","bleedSingleOperation1","bleedSingleOperation2","bleedSwPress1","bleedSwPress2","correctedCoreSpeed1a","correctedCoreSpeed3a","correctedN1Speed1a","correctedN1Speed3a","messageInhibitPhases1","phaseOfFlight1","phaseOfFlightNavigation1","sfyBasFaultWord1Bit131","sfyBasFaultWord1Bit132","pressAltitude1","pressAltitude2","pressAltitude3","pressAltitude4","wOW1", "wOW3" FROM "FlightData"  WHERE "flightFileId" = %s ORDER BY "createdAt" DESC', (flightFileId,))

            result = cur.fetchall()
            cur.close()
            con.close()

            data = {
                "aircraftSerNum1": result[0][0],
                "amscChBasHealthStatus1": result[0][1],
                "amscChBasHealthStatus2": result[0][2],
                "amscHprsovDrivF1": result[0][3],
                "amscHprsovDrivF2": result[0][4],
                "amscPrsovDrivF1": result[0][5],
                "amscPrsovDrivF2": result[0][6],
                "basBleedLowPressF1": result[0][7],
                "basBleedLowPressF2": result[0][8],
                "basBleedLowTempF1": result[0][9],
                "basBleedLowTempF2": result[0][10],
                "basBleedOverPressF1": result[0][11],
                "basBleedOverPressF2": result[0][12],
                "basBleedOverTempF1": result[0][13],
                "basBleedOverTempF2": result[0][14],
                "bleedAcsBleedConfigStatus1": result[0][15],
                "bleedAcsBleedConfigStatus2": result[0][16],
                "bleedFavTmCmd1": result[0][17],
                "bleedFavTmCmd2": result[0][18],
                "bleedFavTmFbk1": result[0][19],
                "bleedFavTmFbk2": result[0][20],
                "bleedHprsovCmdStatus1": result[0][21],
                "bleedHprsovCmdStatus2": result[0][22],
                "bleedHprsovOpPosStatus1": result[0][23],
                "bleedHprsovOpPosStatus2": result[0][24],
                "bleedMonPress1": result[0][25],
                "bleedMonPress2": result[0][26],
                "bleedOnStatus1": result[0][27],
                "bleedOnStatus2": result[0][28],
                "bleedOutTemp1": result[0][29],
                "bleedOutTemp2": result[0][30],
                "bleedOutTempTarget1": result[0][31],
                "bleedOutTempTarget2": result[0][32],
                "bleedOverpressCas1": result[0][33],
                "bleedOverpressCas2": result[0][34],
                "bleedPrecoolDiffPress1": result[0][35],
                "bleedPrecoolDiffPress2": result[0][36],
                "bleedPrsovClPosStatus1": result[0][37],
                "bleedPrsovClPosStatus2": result[0][38],
                "bleedPrsovFbk1": result[0][39],
                "bleedPrsovFbk2": result[0][40],
                "bleedPrsovOpPosStatus1": result[0][41],
                "bleedPrsovOpPosStatus2": result[0][42],
                "bleedPrsovTmCmd1": result[0][43],
                "bleedPrsovTmCmd2": result[0][44],
                "bleedSingleOperation1": result[0][45],
                "bleedSingleOperation2": result[0][46],
                "bleedSwPress1": result[0][47],
                "bleedSwPress2": result[0][48],
                "correctedCoreSpeed1a": result[0][49],
                "correctedCoreSpeed3a": result[0][50],
                "correctedN1Speed1a": result[0][51],
                "correctedN1Speed3a": result[0][52],
                "messageInhibitPhases1": result[0][53],
                "phaseOfFlight1": result[0][54],
                "phaseOfFlightNavigation1": result[0][55],
                "sfyBasFaultWord1Bit131": result[0][56],
                "sfyBasFaultWord1Bit132": result[0][57],
                "pressAltitude1": result[0][58],
                "pressAltitude2": result[0][59],
                "pressAltitude3": result[0][60],
                "pressAltitude4": result[0][61],
                "wOW1": result[0][62],
                "wOW3": result[0][63]
            }
            return data
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def update(flightFileId:str, prediction: int):
        try:
            prediction = str(prediction)

            DB_USER = os.getenv("DB_USER")
            DB_PASSWORD = os.getenv("DB_PASSWORD")
            DB_HOST = os.getenv("DB_HOST")
            DB_PORT = os.getenv("DB_PORT")
            DB_NAME = os.getenv("DB_NAME")

            con = psycopg2.connect(database= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST, port= DB_PORT)

            cur = con.cursor()

            cur.execute('UPDATE "FlightFile" SET "predictionResult" = %s  WHERE "id" = %s ', (prediction,flightFileId,))
            con.commit()
            cur.close()
            con.close()
            return 200, "OK"
        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))






