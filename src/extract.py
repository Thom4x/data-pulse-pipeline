import requests
from typing import List, Dict, Optional

DEFAULT_COIN = "bitcoin"

def fetch_crypto_data(coin_id: str = DEFAULT_COIN) -> Optional[Dict]:
    """
    Extraccion de datos de mercado para una criptomoneda específica desde la API de CoinGecko.

    Args:
        coin_id (str): Identificador de la moneda (ej. 'bitcoin'). 
    Returns:
        Optional[Dict]: Diccionario con datos de mercado o None si hay error
    """

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

if __name__ == "__main__":
    # Prueba 
    data = fetch_crypto_data(DEFAULT_COIN)
    if data:
        print(f"Conexion exitosa, Moneda: {data['name']}")
        print(f"Precio actual: ${data['market_data']['current_price']['usd']}")