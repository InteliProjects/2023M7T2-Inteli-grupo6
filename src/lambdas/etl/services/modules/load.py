from fastapi import HTTPException
import uuid
import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


class Load:
    async def load_parquet(dataframe, file: str):
        try:
            dataframe = pd.DataFrame(dataframe, index=[0])
            print("Carregando dataframe:", dataframe)

            # Conexão com o banco
            con = psycopg2.connect(
                database= DB_NAME,
                user= DB_USER,
                password= DB_PASSWORD,
                host= DB_HOST,
                port= DB_PORT
            )
            cur = con.cursor()

            cur.execute('SELECT * FROM "FlightFile" WHERE "fileName" = %s', (file,))

            # Fetch the results
            file_infos = cur.fetchall()
            file_id = file_infos[0][0]
            print("Id do arquivo:", file_id)

            for index, row in dataframe.iterrows():
                data_dict = row.to_dict()
                data_dict["flightFileId"] = file_id

                # Inserindo dados no banco
                query = '''INSERT INTO "FlightData" (
                    id,
                    "aircraftSerNum1",
                    "amscChBasHealthStatus1",
                    "amscChBasHealthStatus2",
                    "amscHprsovDrivF1",
                    "amscHprsovDrivF2",
                    "amscPrsovDrivF1",
                    "amscPrsovDrivF2",
                    "basBleedLowPressF1",
                    "basBleedLowPressF2",
                    "basBleedLowTempF1",
                    "basBleedLowTempF2",
                    "basBleedOverPressF1",
                    "basBleedOverPressF2",
                    "basBleedOverTempF1",
                    "basBleedOverTempF2",
                    "bleedAcsBleedConfigStatus1",
                    "bleedAcsBleedConfigStatus2",
                    "bleedFavTmCmd1",
                    "bleedFavTmCmd2",
                    "bleedFavTmFbk1",
                    "bleedFavTmFbk2",
                    "bleedHprsovCmdStatus1",
                    "bleedHprsovCmdStatus2",
                    "bleedHprsovOpPosStatus1",
                    "bleedHprsovOpPosStatus2",
                    "bleedMonPress1",
                    "bleedMonPress2",
                    "bleedOnStatus1",
                    "bleedOnStatus2",
                    "bleedOutTemp1",
                    "bleedOutTemp2",
                    "bleedOutTempTarget1",
                    "bleedOutTempTarget2",
                    "bleedOverpressCas1",
                    "bleedOverpressCas2",
                    "bleedPrecoolDiffPress1",
                    "bleedPrecoolDiffPress2",
                    "bleedPrsovClPosStatus1",
                    "bleedPrsovClPosStatus2",
                    "bleedPrsovFbk1",
                    "bleedPrsovFbk2",
                    "bleedPrsovOpPosStatus1",
                    "bleedPrsovOpPosStatus2",
                    "bleedPrsovTmCmd1",
                    "bleedPrsovTmCmd2",
                    "bleedSingleOperation1",
                    "bleedSingleOperation2",
                    "bleedSwPress1",
                    "bleedSwPress2",
                    "correctedCoreSpeed1a",
                    "correctedCoreSpeed3a",
                    "correctedN1Speed1a",
                    "correctedN1Speed3a",
                    "messageInhibitPhases1",
                    "phaseOfFlight1",
                    "phaseOfFlightNavigation1",
                    "sfyBasFaultWord1Bit131",
                    "sfyBasFaultWord1Bit132",
                    "pressAltitude1",
                    "pressAltitude2",
                    "pressAltitude3",
                    "pressAltitude4",
                    "wOW1",
                    "wOW3",
                    "flightFileId"
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s
                );'''


                data=(
                    str(uuid.uuid4()),
                    int(data_dict["aircraftSerNum1"]),
                    data_dict["amscChBasHealthStatus1"],
                    data_dict["amscChBasHealthStatus2"],
                    data_dict["amscHprsovDrivF1"],
                    data_dict["amscHprsovDrivF2"],
                    data_dict["amscPrsovDrivF1"],
                    data_dict["amscPrsovDrivF2"],
                    data_dict["basBleedLowPressF1"],
                    data_dict["basBleedLowPressF2"],
                    data_dict["basBleedLowTempF1"],
                    data_dict["basBleedLowTempF2"],
                    data_dict["basBleedOverPressF1"],
                    data_dict["basBleedOverPressF2"],
                    data_dict["basBleedOverTempF1"],
                    data_dict["basBleedOverTempF2"],
                    data_dict["bleedAcsBleedConfigStatus1"],
                    data_dict["bleedAcsBleedConfigStatus2"],
                    data_dict["bleedFavTmCmd1"],
                    data_dict["bleedFavTmCmd2"],
                    data_dict["bleedFavTmFbk1"],
                    data_dict["bleedFavTmFbk2"],
                    data_dict["bleedHprsovCmdStatus1"],
                    data_dict["bleedHprsovCmdStatus2"],
                    data_dict["bleedHprsovOpPosStatus1"],
                    data_dict["bleedHprsovOpPosStatus2"],
                    data_dict["bleedMonPress1"],
                    data_dict["bleedMonPress2"],
                    data_dict["bleedOnStatus1"],
                    data_dict["bleedOnStatus2"],
                    data_dict["bleedOutTemp1"],
                    data_dict["bleedOutTemp2"],
                    data_dict["bleedOutTempTarget1"],
                    data_dict["bleedOutTempTarget2"],
                    data_dict["bleedOverpressCas1"],
                    data_dict["bleedOverpressCas2"],
                    data_dict["bleedPrecoolDiffPress1"],
                    data_dict["bleedPrecoolDiffPress2"],
                    data_dict["bleedPrsovClPosStatus1"],
                    data_dict["bleedPrsovClPosStatus2"],
                    data_dict["bleedPrsovFbk1"],
                    data_dict["bleedPrsovFbk2"],
                    data_dict["bleedPrsovOpPosStatus1"],
                    data_dict["bleedPrsovOpPosStatus2"],
                    data_dict["bleedPrsovTmCmd1"],
                    data_dict["bleedPrsovTmCmd2"],
                    data_dict["bleedSingleOperation1"],
                    data_dict["bleedSingleOperation2"],
                    data_dict["bleedSwPress1"],
                    data_dict["bleedSwPress2"],
                    data_dict["correctedCoreSpeed1a"],
                    data_dict["correctedCoreSpeed3a"],
                    data_dict["correctedN1Speed1a"],
                    data_dict["correctedN1Speed3a"],
                    data_dict["messageInhibitPhases1"],
                    data_dict["phaseOfFlight1"],
                    data_dict["phaseOfFlightNavigation1"],
                    data_dict["sfyBasFaultWord1Bit131"],
                    data_dict["sfyBasFaultWord1Bit132"],
                    data_dict["pressAltitude1"],
                    data_dict["pressAltitude2"],
                    data_dict["pressAltitude3"],
                    data_dict["pressAltitude4"],
                    data_dict["wOW1"],
                    data_dict["wOW3"],
                    data_dict["flightFileId"]
                )
                print(data)
                cur.execute(query, data)
                con.commit()

            cur.close()
            con.close()
            print("Dados inseridos com sucesso!")
            return file_id

        except Exception as e:
            print(400, str(e))
            raise HTTPException(status_code=400, detail=str(e))
