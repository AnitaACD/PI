import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

# Obtener variables de entorno (con valores por defecto)
server = os.getenv('DB_HOST', 'sqlserver')  # En Docker usa 'sqlserver'
database = os.getenv('DB_NAME', 'GestionActivos')
username = os.getenv('DB_USER', 'sa')
password = os.getenv('SA_PASSWORD', 'SqlServer@123')
driver = "{ODBC Driver 17 for SQL Server}"

# Construir cadena de conexión
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Intentar conectar con timeout mayor
try:
    conn = pyodbc.connect(conn_str, autocommit=True, timeout=30)
    cursor = conn.cursor()
    print("Conexión exitosa a SQL Server")
except Exception as e:
    print(f"Error de conexión: {e}")
    raise