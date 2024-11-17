import pandas as pd
import logging
import os

logging.basicConfig(filename='./log.txt',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%d %m %Y %H:%M:%S',
    level=logging.INFO)

def read_excel_file(file_path, engine='openpyxl', sheet_name=None, skiprows=None):
    logging.info("Reading the Excel file ...")
    return pd.read_excel(file_path, engine=engine, sheet_name=sheet_name, skiprows=skiprows)

def drop_unnecessary_columns(df, columns):
    logging.info("Dropping unnecessary columns ...")
    df.drop(columns=columns, axis=1, inplace=True)

def rename_columns(df, columns):
    logging.info("Renaming specific columns ...")
    df.rename(columns=columns, inplace=True)

def filter_rows(df, countries, start_year, end_year):
    logging.info("Filtering rows ...")
    return df[df['Country'].isin(countries) & (df['Year'] >= start_year) & (df['Year'] <= end_year)]

def reset_index(df):
    logging.info("Resetting the index of the DataFrame ...")
    df.reset_index(drop=True, inplace=True)

def pivot_dataframe(df, index, columns, values):
    logging.info("Pivoting the DataFrame ...")
    df_pivoted = df.pivot(index=index, columns=columns, values=values)
    df_pivoted.reset_index(inplace=True)
    df_pivoted.columns.name = None
    return df_pivoted

def append_suffix_to_columns(df, suffix):
    logging.info(f"Appending '{suffix}' to the country names in the columns ...")
    df.rename(columns=lambda x: x + suffix if x != 'Year' else x, inplace=True)

def delete_file(file_path):
    logging.info(f"Deleting the file: {file_path}")
    os.remove(file_path)

def interpolate_missing_values(df):

    logging.info("Interpolating missing values ...")
    
    # Separate the 'Year' column
    year_column = df['Year']
    other_columns = df.drop(columns=['Year'])

    # Interpolate missing values in other columns
    other_columns = other_columns.interpolate(method='linear', limit_direction='forward', axis=0)

    # Combine the 'Year' column back with the other columns
    df = pd.concat([year_column, other_columns], axis=1)

    return df