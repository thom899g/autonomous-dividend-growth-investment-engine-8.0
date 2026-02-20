import pandas as pd
from typing import Dict, List
from datetime import datetime

class StockScreener:
    def __init__(self, data_source='yahoo'):
        self.data_source = data_source
        self.filtered_stocks = pd.DataFrame()

    def fetch_data(self, symbols: List[str]) -> Dict:
        """Fetches stock data from the specified data source."""
        # Simulated data fetching; in practice, use an API
        data = {symbol: {'price': 100.0, 'div_yield': 3.0} for symbol in symbols}
        return data

    def apply_filters(self, data: Dict) -> pd.DataFrame:
        """Applies screening criteria to filter stocks."""
        df = pd.DataFrame.from_dict(data).T
        df['last_div_date'] = datetime.now()
        filtered = df[df['div_yield'] > 3.0 & df['price'] < 100]
        return filtered

    def get_high_growth_stocks(self, symbols: List[str]) -> pd.DataFrame:
        """Returns high-growth dividend stocks."""
        data = self.fetch_data(symbols)
        return self.apply_filters(data)

# Example usage
if __name__ == '__main__':
    screener = StockScreener()
    stocks = ['AAPL', 'MSFT', 'PEP']
    high_growth_stocks = screener.get_high_growth_stocks(stocks)
    print(high_growth_stocks)