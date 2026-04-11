import pandas as pd
from typing import Dict, Optional

def transform_market_data(raw_data: Dict) -> Optional[pd.DataFrame]:
    """Crea un DataFrame básico a partir de los datos crudos."""
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
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None