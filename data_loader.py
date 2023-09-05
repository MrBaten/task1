import json
from myapp.models import Trade

def load_json_data():
    with open('/Users/mr_baten/Desktop/macdjango/one/jsondata/stock_market_data.json', 'r') as file:
        data = json.load(file)
        for item in data:
            Trade.objects.create(
                date = item['date'],
                trade_code = item['trade_code'],
                high = item['high'],
                low = item['low'],
                open = item['open'],
                close = item['close'],
                volume = item['volume']
            )

load_json_data()