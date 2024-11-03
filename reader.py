# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def csv_as_dicts(lines, types, headers = None):
    def make_dict(headers, row, types = types):
        return { name: func(val) for name, func, val in zip(headers, types, row) }
    return convert_csv(lines, make_dict, headers = headers)
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val) for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
        
def csv_as_instances(file, cls):
    return convert_csv(file, lambda headers, row: cls.from_row(row))
    records = []
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def convert_csv(lines, conversion, headers = None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: conversion(headers, row), rows))
    for row in rows:
        record = conversion(headers, row)
        records.append(record)
    return records

