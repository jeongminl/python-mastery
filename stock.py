# Exercise 3.1

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
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
            row_class = Stock(row[0], int(row[1]), float(row[2]))
            records.append(row_class)
    return records

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print('%10s %10s %10s' % ('----------', '----------','----------')) 
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))