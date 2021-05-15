from morda.models import Coin
import json


def run():
    with open('my_cryptocoins.json') as json_file:
        db = json.loads(json_file.read())
    for coin in db['coins']:
        print(coin)
        c = Coin(coin['name'],
                 coin['amount'],
                 coin['buy_price'],
                 coin['desired_price_fall'],
                 coin['desired_sell_price'],
                 coin['last_prices'])
        c.save()
