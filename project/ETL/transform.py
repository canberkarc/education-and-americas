import pandas as pd
import logging
import os
import traceback
from .transform_helper import *
from retry import retry

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

@retry(tries=3, delay=5, logger=logging)
def transform_GdpData(file_path):

    try:
        logging.info("Starting to transform the GDP data ...")

        # Read the Excel file
        df = read_excel_file(file_path, engine='xlrd', sheet_name='Data', skiprows=3)

        logging.info("Performing transformations ...")

        # Drop unnecessary columns
        columnsToDrop = df.loc[:, 'Country Code':'2001'].columns
        drop_unnecessary_columns(df, columnsToDrop)

        # Rename specific columns
        columnsToRename = {'Country Name': 'Country'}
        rename_columns(df, columnsToRename)

        # Filter rows where Country is Brazil, Colombia, or Peru
        df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru'])]
        
        # Reset the index of the DataFrame
        df.reset_index(drop=True, inplace=True)

        # Melt the DataFrame to have 'Year' as a variable
        df_melted = df.melt(id_vars=['Country'], var_name='Year', value_name='Value')
        
        # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
        df_pivoted = pivot_dataframe(df_melted, 'Year', 'Country', 'Value')

        # Append '_GDP' to the country names in the columns
        append_suffix_to_columns(df_pivoted, '_GDP')

        df_pivoted['Year'] = df_pivoted['Year'].astype(int)

        # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
        df_pivoted = df_pivoted[(df_pivoted['Year'] >= 2002) & (df_pivoted['Year'] <= 2020)]

        logging.info("Transformation completed successfully!")

        # Delete file
        logging.info(f"Deleting the file: {file_path}")
        delete_file(file_path)

        return df_pivoted

    except Exception as e:
        logging.error(traceback.format_exc())   # Log the traceback

@retry(tries=3, delay=5, logger=logging)
def transform_PublicExpenditureData(file_path):

    try:

        logging.info("Starting to transform the Public Expenditure data ...")
        
        # Read the Excel file
        df = read_excel_file(file_path, engine='openpyxl', sheet_name='data')

        logging.info("Performing transformations ...")

        # Drop unnecessary columns
        columnsToDrop =['indicator', 'National Incomes','unit', 'notes_ids', 'source_id']
        drop_unnecessary_columns(df, columnsToDrop)

        # Rename specific columns
        columnsToRename = {'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}
        rename_columns(df, columnsToRename)

        # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
        df = filter_rows(df, ['Brazil', 'Colombia', 'Peru'], 2002, 2020)

        # Sort the DataFrame by Country and Year
        df.sort_values(by=['Country', 'Year'], inplace=True)

        # Reset the index of the DataFrame
        reset_index(df)
        
        # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
        df_pivoted = pivot_dataframe(df, 'Year', 'Country', 'Value')

        # Append '_PublicExpenditure' to the country names in the columns
        append_suffix_to_columns(df_pivoted, '_PublicExpenditure')

        # Interpolate missing values in the DataFrame
        df_pivoted = interpolate_missing_values(df_pivoted)

        logging.info("Transformation completed successfully!")

        # Delete file
        logging.info(f"Deleting the file: {file_path}")
        delete_file(file_path)

        return df_pivoted
    
    except Exception as e:  
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=5, logger=logging)
def transform_EconomicActivityParticipationData(file_path):

    try:
        logging.info("Starting to transform the Economic Activity Participation data ...")

        # Read the Excel file
        df = read_excel_file(file_path, engine='openpyxl', sheet_name='data')

        logging.info("Performing transformations ...")

        # Drop unnecessary columns
        columnsToDrop = ['indicator', 'Geographical area', 'Escolaridad (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id']
        drop_unnecessary_columns(df, columnsToDrop)

        # Rename specific columns
        columnsToRename = {'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}
        rename_columns(df, columnsToRename)

        # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
        df = filter_rows(df, ['Brazil', 'Colombia', 'Peru'], 2002, 2020)

        # Reset the index of the DataFrame
        reset_index(df)

        # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
        df_pivoted = pivot_dataframe(df, 'Year', 'Country', 'Value')

        # Append '_EconomicActivityParticipation' to the country names in the columns
        append_suffix_to_columns(df_pivoted, '_EconomicActivityParticipation')

        # Interpolate missing values in the DataFrame
        df_pivoted = interpolate_missing_values(df_pivoted)

        logging.info("Transformation completed successfully!")

        # Delete file
        logging.info(f"Deleting the file: {file_path}")
        delete_file(file_path)

        return df_pivoted
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=5, logger=logging)
def transform_IlliteracyRateData(file_path):

    try:    
        logging.info("Starting to transform the Illiteracy Rate data ...")
        
        # Read the Excel file
        df = read_excel_file(file_path, engine='openpyxl', sheet_name='data')

        logging.info("Performing transformations ...")

        # Drop unnecessary columns
        columnsToDrop = ['indicator', 'Geographical area', 'Age group by participation in EPA__(15_60_more) (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id']
        drop_unnecessary_columns(df, columnsToDrop)

        # Rename specific columns
        columnsToRename = {'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}
        rename_columns(df, columnsToRename)

        # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
        df = filter_rows(df, ['Brazil', 'Colombia', 'Peru'], 2002, 2020)

        # Reset the index of the DataFrame
        reset_index(df)

        # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
        df_pivoted = pivot_dataframe(df, 'Year', 'Country', 'Value')

        # Append '_IlliteracyRates' to the country names in the columns
        append_suffix_to_columns(df_pivoted, '_IlliteracyRates')

        # Interpolate missing values in the DataFrame
        df_pivoted = interpolate_missing_values(df_pivoted)

        logging.info("Transformation completed successfully!")

        # Delete file
        delete_file(file_path)

        return df_pivoted

    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=5, logger=logging)
def transform_YearsOfEducationData(file_path):
    
    try:    

        logging.info("Starting to transform the Years of Education data ...")

        # Read the Excel file
        df = read_excel_file(file_path, engine='openpyxl', sheet_name='data')

        logging.info("Performing transformations ...")

        # Drop unnecessary columns
        columnsToDrop = ['indicator', 'Geographical area', 'Escolaridad (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id']
        drop_unnecessary_columns(df, columnsToDrop)

        # Rename specific columns
        columnsToRename = {'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}
        rename_columns(df, columnsToRename)

        # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
        df = filter_rows(df, ['Brazil', 'Colombia', 'Peru'], 2002, 2020)

        # Reset the index of the DataFrame
        reset_index(df)

        # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
        df_pivoted = pivot_dataframe(df, 'Year', 'Country', 'Value')

        # Append '_YearsOfEducation' to the country names in the columns
        append_suffix_to_columns(df_pivoted, '_YearsOfEducation')

        # Interpolate missing values in the DataFrame
        df_pivoted = interpolate_missing_values(df_pivoted)

        logging.info("Transformation completed successfully!")

        # Delete file
        logging.info(f"Deleting the file: {file_path}")
        delete_file(file_path)

        return df_pivoted
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

