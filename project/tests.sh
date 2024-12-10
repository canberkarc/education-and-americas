python -m pytest tests.py


# Check if the .db file is created
DB_FILE_PATH="/home/runner/work/education-and-americas/education-and-americas/project/data/educationAndEconomy_BrazilColombiaPeru.db"
if [ -f "$DB_FILE_PATH" ]; then
    echo "$DB_FILE_PATH exists."
else
    echo "$DB_FILE_PATH does not exist."
    exit 1
fi