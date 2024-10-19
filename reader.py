# Section 2.6

import csv
import collections.abc
from abc import ABC, abstractmethod

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_dicts(filename, types):
    parser = DictCSVParser(types)
    return parser.parse(filename)

class DataCollection(collections.abc.Sequence):
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
            ridedata_slice = DataCollection()
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

def read_csv_as_columns(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    return_list = DataCollection()
    headers = next(rows)
    for row in rows:
        return_list.append({name:func(val) for name, func, val in zip(headers, types, row)})
    f.close()
    return return_list

def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)