# readrides.py Exercises 2.1, 2.2, 2.5 

import csv
import collections.abc

class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return { 'route': self.routes[index],
                     'date': self.dates[index],
                     'daytype': self.daytypes[index],
                     'rides': self.numrides[index] }
        
        elif isinstance(index, slice):
            ridedata_slice = RideData()
            ridedata_slice.routes = self.routes[index]
            ridedata_slice.dates = self.dates[index]
            ridedata_slice.daytypes = self.daytypes[index]
            ridedata_slice.numrides = self.numrides[index]
            return ridedata_slice

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = RideData() #[]
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            rides_dict = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(rides_dict)
    return records

def read_rides_as_class(filename):
    class Row_class:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row_class = Row_class(route, date, daytype, rides)
            records.append(row_class)
    return records

def read_rides_as_namedtuple(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    from collections import namedtuple
    Row_namedtuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            rides_namedtuple = Row_namedtuple(route, date, daytype, rides)
            records.append(rides_namedtuple)
    return records

def read_rides_as_slotted_class(filename):
    class Row_class:
        __slots__ = ['route', 'date', 'daytype', 'rides']
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides
    '''
    Read the bus ride data as a list of slotted classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            row_class = Row_class(route, date, daytype, rides)
            records.append(row_class)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('Data/ctabus.csv')
    rows = read_rides_as_dictionary('Data/ctabus.csv')
    #rows = read_rides_as_class('Data/ctabus.csv')
    #rows = read_rides_as_namedtuple('Data/ctabus.csv')
    #rows = read_rides_as_slotted_class('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    r = rows[0:10]
    print(len(r), r[0])
    exit()
    from collections import Counter
    totals = Counter()
    for s in rows:
        totals[s.route] += s.rides
        if s.date == "02/02/2011" and s.rides == "22":
            print(f"{s.rides} people rode the number 22 bus on Feb 2 2011.")
    print(f"{len(totals)} routes exist in Chicago.")
    print(totals.most_common(3))
    #for route in totals:
    #    print(f"{totals[route]} rides are taken in route {route}")
    increase = Counter()
    for s in rows:
        if '2001' in s.date:
            increase[s.route] -= s.rides
        elif '2011' in s.date:
            increase[s.route] += s.rides
    
    print(increase.most_common(5))
    