from .extract import *
from .transform import *
from .load import load_data_to_sqlite
import logging

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

# ETL processes
def DataPipeline():
        
    try:
        logging.info("\nStarting the ETL process...")

        # ETL process for GDP data
        logging.info("\nExtracting and transforming GDP data...")
        path_GdpData = extractGdpData()
        df_Gdp = transform_GdpData(path_GdpData)
        load_data_to_sqlite(df_Gdp, "GDP")

        # ETL process for Public Expenditure data
        logging.info("\nExtracting and transforming Public Expenditure data...")
        path_PublicExpenditureData = extractPublicExpenditureData()
        df_PublicExpenditure = transform_PublicExpenditureData(path_PublicExpenditureData)
        load_data_to_sqlite(df_PublicExpenditure, "PublicExpenditure")

        # ETL process for Economic Activity Participation data
        logging.info("\nExtracting and transforming Economic Activity Participation data...")
        path_EconomicActivityParticipation = extractEconomicActivityParticipationData()
        df_EconomicActivityParticipation = transform_EconomicActivityParticipationData(path_EconomicActivityParticipation)
        load_data_to_sqlite(df_EconomicActivityParticipation, "EconomicActivityParticipation")

        # ETL process for Illiteracy Rate data
        logging.info("\nExtracting and transforming Illiteracy Rate data...")
        path_IlliteracyRateData = extractIlliteracyRateData()
        df_IlliteracyRate =  transform_IlliteracyRateData(path_IlliteracyRateData)
        load_data_to_sqlite(df_IlliteracyRate, "IlliteracyRate")

        # ETL process for Years of Education data
        logging.info("\nExtracting and transforming Years of Education data...")
        path_YearsOfEducationData = extractYearsOfEducationData()
        df_YearsOfEducation = transform_YearsOfEducationData(path_YearsOfEducationData)
        load_data_to_sqlite(df_YearsOfEducation, "YearsOfEducation")


        logging.info("ETL process completed successfully!")

    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback