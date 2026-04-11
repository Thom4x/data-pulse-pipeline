import sqlite3
import pandas as pd
from datetime import datetime

def load_to_sqlite(df: pd.DataFrame, db_name: str = "data/crypto_database.db"):
    """
    Carga un DataFrame de Pandas en una tabla de SQLite.
    """
    try:
        # Crear la conexion
        conn = sqlite3.connect(db_name)
        
        # Cargamos los datos en la tabla 'prices'
        df.to_sql('prices', conn, if_exists='append', index=False)
        
        conn.close()
        print(f"Datos cargados exitosamente en {db_name} a las {datetime.now().strftime('%H:%M:%S')}")
        
    except Exception as e:
        print(f"Error al cargar en la base de datos: {e}")

if __name__ == "__main__":
    # Prueba 
    test_df = pd.DataFrame({
        'coin_name': ['Bitcoin'],
        'symbol': ['BTC'],
        'current_price_usd': [65000.50],
        'market_cap_usd': [1200000000000],
        'last_updated': [pd.to_datetime('now')]
    })
    load_to_sqlite(test_df)