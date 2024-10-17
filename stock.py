# Exercise 3.1 and 3.3

class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @property
    def price(self):
        return self._price

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1]}")
        elif value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2]}")
        elif value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    
    def sell(self, amt):
        self.shares -= amt

def read_portfolio(filename):
    import csv
    '''
    Read the data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            row_class = Stock.from_row(row[0], row[1], row[2])
            records.append(row_class)
    return records

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('%10s %10s %10s' % ('----------', '----------','----------')) 
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))