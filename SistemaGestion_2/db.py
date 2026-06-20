import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

server = os.getenv('DB_HOST', 'sqlserver')
database = os.getenv('DB_NAME', 'GestionActivos')
username = os.getenv('DB_USER', 'sa')
password = os.getenv('DB_PASSWORD')

if not password:
    raise RuntimeError("Falta la variable de entorno DB_PASSWORD en tu .env")

driver = "{ODBC Driver 17 for SQL Server}"
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(conn_str, autocommit=True, timeout=30)
    cursor = conn.cursor()
    print("Conexión exitosa a SQL Server")
except Exception as e:
    print(f"Error de conexión: {e}")
    raise

def get_cursor():
    """Devuelve el cursor activo de la conexión a SQL Server."""
    return cursor