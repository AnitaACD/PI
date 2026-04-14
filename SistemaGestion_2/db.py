import os
import pyodbc

server = os.getenv('DB_HOST', 'localhost') + ',' + os.getenv('DB_PORT', '14334')
database = os.getenv('DB_NAME', 'GestionActivos')
username = os.getenv('DB_USER', 'sa')
password = os.getenv('DB_PASSWORD', 'SqlServer@123')
driver = "ODBC Driver 17 for SQL Server"
conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(conn_str, autocommit=True, timeout=30)
    cursor = conn.cursor()
    print("Conexión exitosa a SQL Server")
except Exception as e:
    print(f"Error de conexión: {e}")
    conn = None
    cursor = None
