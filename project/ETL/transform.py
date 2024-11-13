import pandas as pd
import logging
import os

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)


def transform_IlliteracyRateData(file_path):
    
    logging.info("Starting to transform the Illiteracy Rate data ...")
    
    # Read the Excel file
    logging.info("Reading the Excel file ...")
    df = pd.read_excel(file_path, engine='openpyxl')

    logging.info("Performing transformations ...")

    # Drop unnecessary columns
    df.drop(columns=['indicator', 'Geographical area', 'Age group by participation in EPA__(15_60_more) (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id'], axis=1, inplace=True)

    # Rename specific columns
    df.rename(columns={'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}, inplace=True)

    # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
    df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru']) & (df['Year'] >= 2002) & (df['Year'] <= 2020)]

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
    df_pivoted = df.pivot(index='Year', columns='Country', values='Value')

    # Reset the index of the pivoted DataFrame
    df_pivoted.reset_index(inplace=True)

    # Remove the name attribute from the columns
    df_pivoted.columns.name = None

    # Append '_IlliteracyRates' to the country names in the columns
    df_pivoted.rename(columns=lambda x: x + '_IlliteracyRates' if x != 'Year' else x, inplace=True)

    logging.info("Transformation completed successfully!")

    # Delete file
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

    return df_pivoted


def transform_YearsOfEducationData(file_path):

    logging.info("Starting to transform the Years of Education data ...")

    # Read the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')

    logging.info("Performing transformations ...")

    # Drop unnecessary columns
    df.drop(columns=['indicator', 'Geographical area', 'Escolaridad (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id'], axis=1, inplace=True)

    # Rename specific columns
    df.rename(columns={'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}, inplace=True)

    # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
    df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru']) & (df['Year'] >= 2002) & (df['Year'] <= 2020)]

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
    df_pivoted = df.pivot(index='Year', columns='Country', values='Value')

    # Reset the index of the pivoted DataFrame
    df_pivoted.reset_index(inplace=True)

    # Remove the name attribute from the columns
    df_pivoted.columns.name = None

    # Append '_YearsOfEducation' to the country names in the columns
    df_pivoted.rename(columns=lambda x: x + '_YearsOfEducation' if x != 'Year' else x, inplace=True)

    logging.info("Transformation completed successfully!")

    # Delete file
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

    return df_pivoted


def transform_EconomicActivityParticipationData(file_path):

    logging.info("Starting to transform the Economic Activity Participation data ...")

    # Read the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')

    logging.info("Performing transformations ...")

    # Drop unnecessary columns
    df.drop(columns=['indicator', 'Geographical area', 'Escolaridad (HS)', 'Sex__ESTANDAR', 'unit', 'notes_ids', 'source_id'], axis=1, inplace=True)

    # Rename specific columns
    df.rename(columns={'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}, inplace=True)

    # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
    df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru']) & (df['Year'] >= 2002) & (df['Year'] <= 2020)]

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
    df_pivoted = df.pivot(index='Year', columns='Country', values='Value')

    # Reset the index of the pivoted DataFrame
    df_pivoted.reset_index(inplace=True)

    # Remove the name attribute from the columns
    df_pivoted.columns.name = None

    # Append '_EconomicActivityParticipation' to the country names in the columns
    df_pivoted.rename(columns=lambda x: x + '_EconomicActivityParticipation' if x != 'Year' else x, inplace=True)

    logging.info("Transformation completed successfully!")

    # Delete file
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

    return df_pivoted


def transform_PublicExpenditureData(file_path):

    logging.info("Starting to transform the Public Expenditure data ...")
    
    # Read the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')

    logging.info("Performing transformations ...")

    # Drop unnecessary columns
    df.drop(columns=['indicator', 'National Incomes','unit', 'notes_ids', 'source_id'], axis=1, inplace=True)

    # Rename specific columns
    df.rename(columns={'Country__ESTANDAR': 'Country', 'Years__ESTANDAR': 'Year', 'value': 'Value'}, inplace=True)

    # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
    df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru']) & (df['Year'] >= 2002) & (df['Year'] <= 2020)]

    # Sort the DataFrame by Country and Year
    df.sort_values(by=['Country', 'Year'], inplace=True)

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)
    
    # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
    df_pivoted = df.pivot(index='Year', columns='Country', values='Value')

    # Reset the index of the pivoted DataFrame
    df_pivoted.reset_index(inplace=True)

    # Remove the name attribute from the columns
    df_pivoted.columns.name = None

    # Append '_PublicExpenditure' to the country names in the columns
    df_pivoted.rename(columns=lambda x: x + '_PublicExpenditure' if x != 'Year' else x, inplace=True)

    logging.info("Transformation completed successfully!")

    # Delete file
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

    return df_pivoted


def transform_GdpData(file_path):

    logging.info("Starting to transform the GDP data ...")

    # Read the Excel file
    df = pd.read_excel(file_path, engine='xlrd', sheet_name='Data', skiprows=3)

    logging.info("Performing transformations ...")

    # Drop unnecessary columns
    columns_to_drop = df.loc[:, 'Country Code':'2001'].columns
    df.drop(columns=columns_to_drop, axis=1, inplace=True)

    # Rename specific columns
    df.rename(columns={'Country Name': 'Country'}, inplace=True)
    
    # Filter rows where Country is Brazil, Colombia, or Peru
    df = df[df['Country'].isin(['Brazil', 'Colombia', 'Peru'])]

    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Melt the DataFrame to have 'Year' as a variable
    df_melted = df.melt(id_vars=['Country'], var_name='Year', value_name='Value')

    # Pivot the DataFrame to have 'Country' as columns and 'Year' as rows
    df_pivoted = df_melted.pivot(index='Year', columns='Country', values='Value')

    # Reset the index of the pivoted DataFrame
    df_pivoted.reset_index(inplace=True)

    # Remove the name attribute from the columns
    df_pivoted.columns.name = None

    # Append '_GDP' to the country names in the columns
    df_pivoted.rename(columns=lambda x: x + '_GDP' if x != 'Year' else x, inplace=True)

    df_pivoted['Year'] = df_pivoted['Year'].astype(int)

    # Filter rows where Country is Brazil, Colombia, or Peru and Year is between 2002 and 2020 (inclusive)
    df_pivoted = df_pivoted[(df_pivoted['Year'] >= 2002) & (df_pivoted['Year'] <= 2020)]

    logging.info("Transformation completed successfully!")

    # Delete file
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

    return df_pivoted
