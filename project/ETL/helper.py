from .extract import *
from .transform import *
from .load import load_data_to_sqlite
import logging

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

def DataPipeline():
    logging.info("Starting the ETL process...")

    # Extract and transform GDP data
    logging.info("Extracting and transforming GDP data...")
    path_GdpData = extractGdpData()
    df_Gdp = transform_GdpData(path_GdpData)

    # Extract and transform Illiteracy Rate data
    logging.info("Extracting and transforming Illiteracy Rate data...")
    path_PublicExpenditureData = extractPublicExpenditureData()
    df_PublicExpenditure = transform_PublicExpenditureData(path_PublicExpenditureData)

    # Extract and transform Public Expenditure data
    logging.info("Extracting and transforming Years of Education data...")
    path_EconomicActivityParticipation = extractEconomicActivityParticipationData()
    df_EconomicActivityParticipation = transform_EconomicActivityParticipationData(path_EconomicActivityParticipation)

    # Extract and transform Economic Activity Participation data
    logging.info("Extracting and transforming Economic Activity Participation data...")
    path_IlliteracyRateData = extractIlliteracyRateData()
    df_IlliteracyRate =  transform_IlliteracyRateData(path_IlliteracyRateData)

    # Extract and transform Years of Education data
    logging.info("Extracting and transforming Years of Education data...")
    path_YearsOfEducationData = extractYearsOfEducationData()
    df_YearsOfEducation = transform_YearsOfEducationData(path_YearsOfEducationData)

    logging.info("Merging the transformed DataFrames...")
    df_final = df_IlliteracyRate.merge(df_YearsOfEducation, on='Year', how='outer') \
                                .merge(df_EconomicActivityParticipation, on='Year', how='outer') \
                                .merge(df_PublicExpenditure, on='Year', how='outer') \
                                .merge(df_Gdp, on='Year', how='outer')

    logging.info("Loading the final DataFrame to the SQLite database...")
    load_data_to_sqlite(df_final)

    logging.info("ETL process completed successfully!")