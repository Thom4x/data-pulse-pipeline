import pandas as pd
from typing import Dict, Optional

def transform_market_data(raw_data: Dict) -> Optional[pd.DataFrame]:
    """Crea un DataFrame básico a partir de los datos crudos."""
    try:
        data_dict = {
            'coin_name': [raw_data.get('name')],
            'symbol': [raw_data.get('symbol')],
            'price': [raw_data['market_data']['current_price']['usd']],
            'updated': [raw_data['market_data']['last_updated']]
        }
        return pd.DataFrame(data_dict)
    except Exception as e:
        print(f"Error: {e}")
        return None