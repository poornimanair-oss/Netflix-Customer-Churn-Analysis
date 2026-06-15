from sqlalchemy import create_engine

server = "localhost"
database = "NetflixChurn"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as e:
    print("Error:", e)