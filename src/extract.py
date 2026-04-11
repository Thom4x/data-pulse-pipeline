import requests
from typing import List, Dict, Optional

def fetch_crypto_data(coin_id: str = 'bitcoin') -> Optional[Dict]:
    """
    Extraccion de datos de mercado para una criptomoneda específica desde la API de CoinGecko.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

if __name__ == "__main__":
    # Prueba 
    data = fetch_crypto_data('bitcoin')
    if data:
        print(f"Conexion exitosa, Moneda: {data['name']}")
        print(f"Precio actual: ${data['market_data']['current_price']['usd']}")