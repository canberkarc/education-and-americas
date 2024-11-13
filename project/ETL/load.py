import sqlite3
import logging

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

#This function saves a pandas DataFrame to a SQLite database file in the ./data directory.
def load_data_to_sqlite(df, table):
  
    # Create a connection to the SQLite database
    logging.info("Creating a connection to the SQLite database...")
    conn = sqlite3.connect('./data/education_and_americas.db')

    # Save the DataFrame to the SQLite database
    logging.info("Saving the DataFrame to the SQLite database...")
    df.to_sql(table, conn, if_exists='replace', index=False)

    logging.info("Data saved successfully!")

    # Close the connection
    conn.close()

