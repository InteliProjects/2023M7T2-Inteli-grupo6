from scipy import stats
import pandas as pd
import numpy as np



class Transform():
    @staticmethod
    def preprocessing(dataframe):
        dataframe.columns = dataframe.columns.str.replace('-', '')
        dataframe.fillna(0, inplace=True)
        dataframe.drop_duplicates(inplace=True)
        return dataframe

    @staticmethod
    def get_columns(dataframe):
        new_df = pd.DataFrame()
        new_df['recording_time'] = dataframe['recording_time']
        new_df['aircraftSerNum1'] = dataframe['aircraftSerNum1']
        new_df['amscChBasHealthStatus1'] = dataframe['amscChBasHealthStatus1b'] + \
            dataframe['amscChBasHealthStatus1a']
        new_df['amscChBasHealthStatus2'] = dataframe['amscChBasHealthStatus2b']

        new_df['amscHprsovDrivF1'] = dataframe['amscHprsovDrivF1b']
        new_df['amscHprsovDrivF2'] = dataframe['amscHprsovDrivF2b']

        new_df['amscPrsovDrivF1'] = dataframe['amscPrsovDrivF1a'] + \
            dataframe['amscPrsovDrivF1b']

        new_df['amscPrsovDrivF2'] = dataframe['amscPrsovDrivF2b']

        new_df['basBleedLowPressF1'] = dataframe['basBleedLowPressF1a']
        new_df['basBleedLowPressF2'] = dataframe['basBleedLowPressF2b']

        new_df['basBleedLowTempF1'] = dataframe['basBleedLowTempF1a']
        new_df['basBleedLowTempF2'] = dataframe['basBleedLowTempF2b']

        new_df['basBleedOverPressF1'] = dataframe['basBleedOverPressF1a']
        new_df['basBleedOverPressF2'] = dataframe['basBleedOverPressF2b']

        new_df['basBleedOverTempF1'] = dataframe['basBleedOverTempF1a']
        new_df['basBleedOverTempF2'] = dataframe['basBleedOverTempF2b']

        new_df['bleedAcsBleedConfigStatus1'] = dataframe['bleedAcsBleedConfigStatus1b']
        new_df['bleedAcsBleedConfigStatus2'] = dataframe['bleedAcsBleedConfigStatus2b']

        new_df['bleedFavTmCmd1'] = dataframe['bleedFavTmCmd1a'] + \
            dataframe['bleedFavTmCmd1b']
        new_df['bleedFavTmCmd2'] = dataframe['bleedFavTmCmd2b'] + \
            dataframe['bleedFavTmCmd2a']

        new_df['bleedFavTmFbk1'] = dataframe['bleedFavTmFbk1a'] + \
            dataframe['bleedFavTmFbk1b']
        new_df['bleedFavTmFbk2'] = dataframe['bleedFavTmFbk2b']

        new_df['bleedHprsovCmdStatus1'] = dataframe['bleedHprsovCmdStatus1b'] + \
            dataframe['bleedHprsovCmdStatus1a']
        new_df['bleedHprsovCmdStatus2'] = dataframe['bleedHprsovCmdStatus2b'] + \
            dataframe['bleedHprsovCmdStatus2a']

        new_df['bleedHprsovOpPosStatus1'] = dataframe['bleedHprsovOpPosStatus1b'] + \
            dataframe['bleedHprsovOpPosStatus1a']
        new_df['bleedHprsovOpPosStatus2'] = dataframe['bleedHprsovOpPosStatus2b'] + \
            dataframe['bleedHprsovOpPosStatus2a']

        new_df['bleedMonPress1'] = dataframe['bleedMonPress1b'] + \
            dataframe['bleedMonPress1a']
        new_df['bleedMonPress2'] = dataframe['bleedMonPress2b'] + \
            dataframe['bleedMonPress2a']

        new_df['bleedOnStatus1'] = dataframe['bleedOnStatus1b'] + \
            dataframe['bleedOnStatus1a']
        new_df['bleedOnStatus2'] = dataframe['bleedOnStatus2b']

        new_df['bleedOutTemp1'] = dataframe['bleedOutTemp1b'] + \
            dataframe['bleedOutTemp1a']
        new_df['bleedOutTemp2'] = dataframe['bleedOutTemp2b'] + \
            dataframe['bleedOutTemp2a']

        new_df['bleedOutTempTarget1'] = dataframe['bleedOutTempTarget1b'] + \
            dataframe['bleedOutTempTarget1a']
        new_df['bleedOutTempTarget2'] = dataframe['bleedOutTempTarget2b']

        new_df['bleedOverpressCas1'] = dataframe['bleedOverpressCas1a']
        new_df['bleedOverpressCas2'] = dataframe['bleedOverpressCas2b'] + \
            dataframe['bleedOverpressCas2a']

        new_df['bleedPrecoolDiffPress1'] = dataframe['bleedPrecoolDiffPress1b'] + \
            dataframe['bleedPrecoolDiffPress1a']
        new_df['bleedPrecoolDiffPress2'] = dataframe['bleedPrecoolDiffPress2b'] + \
            dataframe['bleedPrecoolDiffPress2a']

        new_df['bleedPrsovClPosStatus1'] = dataframe['bleedPrsovClPosStatus1a']
        new_df['bleedPrsovClPosStatus2'] = dataframe['bleedPrsovClPosStatus2a']

        new_df['bleedPrsovFbk1'] = dataframe['bleedPrsovFbk1a'] + \
            dataframe['bleedPrsovFbk1b']
        new_df['bleedPrsovFbk2'] = dataframe['bleedPrsovFbk2b']

        new_df['bleedPrsovOpPosStatus1'] = dataframe['bleedPrsovOpPosStatus1a'] + \
            dataframe['bleedPrsovOpPosStatus1b']
        new_df['bleedPrsovOpPosStatus2'] = dataframe['bleedPrsovOpPosStatus2a'] + \
            dataframe['bleedPrsovOpPosStatus2b']
        new_df['bleedPrsovTmCmd1'] = dataframe['bleedPrsovTmCmd1a'] + \
            dataframe['bleedPrsovTmCmd1b']
        new_df['bleedPrsovTmCmd2'] = dataframe['bleedPrsovTmCmd2a'] + \
            dataframe['bleedPrsovTmCmd2b']

        new_df['bleedSingleOperation1'] = dataframe['bleedSingleOperation1a']
        new_df['bleedSingleOperation2'] = dataframe['bleedSingleOperation2b']

        new_df['bleedSwPress1'] = dataframe['bleedSwPress1a'] + \
            dataframe['bleedSwPress1b']
        new_df['bleedSwPress2'] = dataframe['bleedSwPress2b'] + \
            dataframe['bleedSwPress2a']

        new_df['correctedCoreSpeed1a'] = dataframe['correctedCoreSpeed1a']
        new_df['correctedCoreSpeed3a'] = dataframe['correctedCoreSpeed3a']
        new_df['correctedN1Speed1a'] = dataframe['correctedN1Speed1a']
        new_df['correctedN1Speed3a'] = dataframe['correctedN1Speed3a']


        new_df['messageInhibitPhases1'] = dataframe['messageInhibitPhases1']
        new_df['phaseOfFlight1'] = dataframe['phaseOfFlight1']
        new_df['phaseOfFlightNavigation1'] = dataframe['phaseOfFlightNavigation1']
        new_df['sfyBasFaultWord1Bit131'] = dataframe['sfyBasFaultWord1Bit131a']
        new_df['sfyBasFaultWord1Bit132'] = dataframe['sfyBasFaultWord1Bit132b']

        new_df['pressAltitude1'] = dataframe['pressAltitude1a']
        new_df['pressAltitude2'] = dataframe['pressAltitude2a']
        new_df['pressAltitude3'] = dataframe['pressAltitude3a']
        new_df['pressAltitude4'] = dataframe['pressAltitude4a']
        new_df['wOW1'] = dataframe['wOW1a']
        new_df['wOW3'] = dataframe['wOW3a']
        dataframe = None
        return new_df

    @staticmethod
    def agg_methods(dataframe):
        z_scores = stats.zscore(dataframe['recording_time'])
        limite_z = 3
        indices_outliers = abs(z_scores) > limite_z
        dataframe = dataframe[~indices_outliers]

        agg_dict = {
            "aircraftSerNum1": "max",
            "amscChBasHealthStatus1": "median",
            "amscChBasHealthStatus2": "median",
            "amscHprsovDrivF1": "median",
            "amscHprsovDrivF2": "median",
            "amscPrsovDrivF1": "median",
            "amscPrsovDrivF2": "median",
            "basBleedLowPressF1": "median",
            "basBleedLowPressF2": "median",
            "basBleedLowTempF1": "max",
            "basBleedLowTempF2": "max",
            "basBleedOverPressF1": "max",
            "basBleedOverPressF2": "max",
            "basBleedOverTempF1": "max",
            "basBleedOverTempF2": "max",
            "bleedAcsBleedConfigStatus1": "max",
            "bleedAcsBleedConfigStatus2": "max",
            "bleedFavTmCmd1": "sum",
            "bleedFavTmCmd2": "sum",
            "bleedFavTmFbk1": "sum",
            "bleedFavTmFbk2": "sum",
            "bleedHprsovCmdStatus1": "max",
            "bleedHprsovCmdStatus2": "max",
            "bleedHprsovOpPosStatus1": "max",
            "bleedHprsovOpPosStatus2": "max",
            "bleedMonPress1": "median",
            "bleedMonPress2": "median",
            "bleedOnStatus1": "median",
            "bleedOnStatus2": "median",
            "bleedOutTemp1": "max",
            "bleedOutTemp2": "max",
            "bleedOutTempTarget1": "sum",
            "bleedOutTempTarget2": "sum",
            "bleedOverpressCas1": "max",
            "bleedOverpressCas2": "max",
            "bleedPrecoolDiffPress1": "median",
            "bleedPrecoolDiffPress2": "median",
            "bleedPrsovClPosStatus1": "max",
            "bleedPrsovClPosStatus2": "max",
            "bleedPrsovFbk1": "median",
            "bleedPrsovFbk2": "median",
            "bleedPrsovOpPosStatus1": "max",
            "bleedPrsovOpPosStatus2": "max",
            "bleedPrsovTmCmd1": "median",
            "bleedPrsovTmCmd2": "median",
            "bleedSingleOperation1": "max",
            "bleedSingleOperation2": "max",
            "bleedSwPress1": "median",
            "bleedSwPress2": "median",
            "correctedCoreSpeed1a": "median",
            "correctedCoreSpeed3a": "median",
            "correctedN1Speed1a": "median",
            "correctedN1Speed3a": "median",
            "messageInhibitPhases1": "max",
            "phaseOfFlight1": "median",
            "phaseOfFlightNavigation1": "max",
            "sfyBasFaultWord1Bit131": "mean",
            "sfyBasFaultWord1Bit132": "mean",
            "pressAltitude1": "median",
            "pressAltitude2": "median",
            "pressAltitude3": "median",
            "pressAltitude4": "median",
            "wOW1": "max",
            "wOW3": "max",
        }

        df_agrupado = dataframe.agg(agg_dict)

        return df_agrupado

    @staticmethod
    def transform_parquet(dataframe):
        dataframe = Transform.preprocessing(dataframe=dataframe)
        dataframe = Transform.get_columns(dataframe=dataframe)
        dataframe = Transform.agg_methods(dataframe=dataframe)
        return dataframe.to_dict()
