# hello test
import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("netflix_cleaned.csv")

# SQL Server connection
server = "localhost"
database = "NetflixChurn"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load data into SQL table
df.to_sql(
    "netflix_customers",
    con=engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")