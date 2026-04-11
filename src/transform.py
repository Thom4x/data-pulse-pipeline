import pandas as pd
from typing import Dict, Optional

def transform_market_data(raw_data: Dict) -> Optional[pd.DataFrame]:
    """
    Limpia y estructura los datos crudos de la API.
    
    Args:
        raw_data (Dict): Datos en formato JSON obtenidos de la API.
        
    Returns:
        Optional[pd.DataFrame]: DataFrame con tipos de datos corregidos o None si falla.
    
    """

    if not raw_data:
        return None

    try:
        data_dict = {
            'coin_name': [raw_data.get('name')],
            'current_price_usd': [raw_data['market_data']['current_price']['usd']],
            'market_cap_usd': [raw_data['market_data']['market_cap']['usd']],
            'last_updated': [raw_data['market_data']['last_updated']],
            'symbol': [raw_data.get('symbol', '').upper()],
        }
        df = pd.DataFrame(data_dict)
        df['current_price_usd'] = df['current_price_usd'].round(2)
        df['last_updated'] = pd.to_datetime(df['last_updated'])
        return df
    
    except KeyError as e:
        print(f"Error: No se encontró la llave {e} en la respuesta de la API.")
        return None
    
    except Exception as e:
        print(f"Error inesperado en la transformación: {e}")
        return None
    
