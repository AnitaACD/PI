# db.py
import pyodbc

server = "localhost,14333"  # ej: localhost\SQLEXPRESS
database = "GestionActivos"
username = "sa"
password = "SqlServer@123"
driver = "ODBC Driver 17 for SQL Server"

conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(conn_str, autocommit=True)
cursor = conn.cursor()
