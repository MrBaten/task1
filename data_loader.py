import json
from myapp.models import Person

def load_json_data():
    with open('stock_market_data.json', 'r') as file:
        data = json.load(file)
        for item in data:
            Person.objects.create(
                date = item['date'],
                trade_code = item['trade_code'],
                high = item['high'],
                low = item['low'],
                open = item['open'],
                close = item['close'],
                volume = item['volume']
            )

load_json_data()