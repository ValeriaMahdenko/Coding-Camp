from Validation import Validation
from CurrencyConverter import CurrencyConverter
import operator


class Ccy:
    def __init__(self, suma, currency):
        self.suma = suma
        self.currency = currency

    @property
    def suma(self):
        return self._suma

    @suma.setter
    @Validation.decorator_price
    def suma(self, value):
        self._suma = float(value)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    @Validation.decorator_string
    def currency(self, value):
        self._currency = value.upper()

    def __str__(self):
        return f'Money: {self.suma} {self.currency} '

    @staticmethod
    def all(self, other, operation):
        try:
            if str(other).isdigit():
                return operation(self.suma, other)
            else:
                el = CurrencyConverter()
                new_suma = el.convert(other.currency,
                                      self.currency, other.suma)
                return operation(self.suma, new_suma)
        except KeyError as e:
            print(e)

    # instance == other
    def __eq__(self, other):
        return Ccy.all(self, other, operator.eq)

    # instance < other
    def __lt__(self, other):
        return Ccy.all(self, other, operator.lt)

    # instance > other
    def __gt__(self, other):
        return Ccy.all(self, other, operator.gt)

    # instance + other
    def __add__(self, other):
        return Ccy(round(Ccy.all(self, other, operator.add), 2), self.currency)

    # instance - other
    def __sub__(self, other):
        return Ccy(round(Ccy.all(self, other, operator.sub), 2), self.currency)

    # instance * other
    def __mul__(self, other):
        return Ccy(round(Ccy.all(self, other, operator.mul), 2), self.currency)

    # instance / other
    def __truediv__(self, other):
        return Ccy(
            round(Ccy.all(self, other, operator.truediv), 2), self.currency)

    def convert_in(self, to_currenty: str):
        try:
            el = CurrencyConverter()
            return Ccy(round(
                el.convert(self.currency, to_currenty.upper(), self.suma), 2),
                       to_currenty)
        except KeyError as e:
            print(e)
