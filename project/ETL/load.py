import sqlite3
import logging
import traceback
import os

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

#This function saves a pandas DataFrame to a SQLite database file in the ./data directory.
def load_data_to_sqlite(df, table):

    try:
        # Create a connection to the SQLite database
        logging.info("Creating a connection to the SQLite database...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.abspath(os.path.join(script_dir, '..', '..'))
        data_dir = os.path.join(base_dir, 'data')
        db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')
        conn = sqlite3.connect(db_file_path)

        # Save the DataFrame to the SQLite database
        logging.info("Saving the DataFrame to the SQLite database...")
        df.to_sql(table, conn, if_exists='replace', index=False)

        logging.info("Data saved successfully!")

        # Close the connection
        conn.close()

    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

