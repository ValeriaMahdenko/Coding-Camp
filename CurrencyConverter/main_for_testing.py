from Ccy import Ccy

v1 = Ccy(10, "usd")   # automatically usd = USD
v2 = Ccy(10.50, "USD")
print(v1)
print(v1 == v2)
print(v1 > v2)
print(v1 < v2)
print(v1 < 50)

v3 = Ccy(100, "EUR")
v4 = Ccy(30, "USD")
print(v3+v4)
print(v3-v4)
print(v3*v4)
print(v3/v4)
print(v4+4)

print(v3+v4-v4)
v5 = Ccy(130, 'USD')
print(v5.convert_in('PLN'))
