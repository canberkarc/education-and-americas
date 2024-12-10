from data_pipeline import main
import os
import sqlite3
import pytest

def test_data_pipeline():

    # Determine the path to the .db file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(base_dir, 'data')
    db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')

    # Delete the .db file if it exists
    if os.path.exists(db_file_path):
        os.remove(db_file_path)

    # Run the data pipeline
    main()

    # Check if the .db file is created
    assert os.path.exists(db_file_path), f"{db_file_path} does not exist"

    print("Data pipeline test passed and .db file created successfully.")


def test_db_tables():

    # Determine the path to the .db file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(base_dir, 'data')
    db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')

    # Delete the .db file if it exists
    if os.path.exists(db_file_path):
        os.remove(db_file_path)

    # Run the data pipeline
    main()

    # base_dir = os.getcwd()
    # data_dir = os.path.abspath(os.path.join(base_dir, '..', 'data'))
    # db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # List of expected tables
    expected_tables = [
        "EconomicActivityParticipation",
        "GDP",
        "IlliteracyRate",
        "PublicExpenditure",
        "YearsOfEducation"
    ]

    # Get the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    tables = [table[0] for table in tables]

    # Check if all expected tables are present
    for table in expected_tables:
        assert table in tables, f"Table {table} does not exist in the database"

    # Close the database connection
    conn.close()

    print("Data pipeline test passed and all expected tables are present in the .db file.")


def test_table_structure():

    # Determine the path to the .db file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(base_dir, 'data')
    db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')

    # Delete the .db file if it exists
    if os.path.exists(db_file_path):
        os.remove(db_file_path)


    # Run the data pipeline
    main()

    # base_dir = os.getcwd()
    # data_dir = os.path.abspath(os.path.join(base_dir, '..', 'data'))
    # db_file_path = os.path.join(data_dir, 'educationAndEconomy_BrazilColombiaPeru.db')
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # List of expected tables
    expected_tables = [
        "EconomicActivityParticipation",
        "GDP",
        "IlliteracyRate",
        "PublicExpenditure",
        "YearsOfEducation"
    ]

    # Check the structure of each table
    for table in expected_tables:
        # Check the number of columns
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        assert len(columns) == 4, f"Table {table} does not have 4 columns"

        # Check the number of rows
        cursor.execute(f"SELECT COUNT(*) FROM {table};")
        row_count = cursor.fetchone()[0]
        assert row_count == 19, f"Table {table} does not have 19 rows"

    # Close the database connection
    conn.close()

    print("Data pipeline test passed and all tables have the correct structure.")

print()