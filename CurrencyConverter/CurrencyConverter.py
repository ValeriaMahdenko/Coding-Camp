import requests
from secret_info import url
# File secret_info is private


class CurrencyConverter:
    """ Based on https://fixer.io/ """
    def __init__(self):
        self.currencies = requests.get(url).json()
        self.rates = self.currencies['rates']

    def convert(self, from_currency, to_currency, amount):
        try:
            if from_currency != 'EUR':
                amount = amount / self.rates[from_currency]
            converted = amount * self.rates[to_currency]
            return converted
        except KeyError:
            raise KeyError("Currency incorrect")
