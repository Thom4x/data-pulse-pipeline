from src.extract import fetch_crypto_data
from src.transform import transform_market_data
from src.load import load_to_sqlite
import os

def run_pipeline(coin_id="bitcoin"):
    print(f"--- Iniciando Pipeline para: {coin_id.upper()} ---")
    
    # 1. EXTRACCIÓN
    raw_data = fetch_crypto_data(coin_id)
    if not raw_data:
        print("Error en la extracción.")
        return
    
    print("Extracción completada...")

    # 2. TRANSFORMACIÓN
    clean_df = transform_market_data(raw_data)
    if clean_df is None: return

    # 3. CARGA
    if not os.path.exists('data'):
        os.makedirs('data')

    load_to_sqlite(clean_df)
    print("--- Pipeline finalizado ---")

if __name__ == "__main__":
    # Procesar varias cripto
    coins = ["bitcoin", "ethereum", "solana"]
    
    for coin in coins:
        run_pipeline(coin)