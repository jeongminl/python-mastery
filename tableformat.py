# Exercise 3.2 and 3.5
from abc import ABC, abstractmethod
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join('%s' % h for h in headers))
    
    def row(self, rowdata):
        print(','.join('%s' % r for r in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        print(' '.join('<th>%s</th>' % h for h in headers), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        print(' '.join('<td>%s</td>' % r for r in rowdata), end='')
        print('</tr>')

def create_formatter(choice):
    import stock, reader, tableformat
    if choice.lower() == 'text':
        return TextTableFormatter()
    elif choice.lower() == 'csv':
        return CSVTableFormatter()
    elif choice.lower() == 'html':
        return HTMLTableFormatter()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

'''
def print_table(table, attr):
    for att in attr:
        print('%10s' % (att), end='')
    print()
    print(('-'*10 + ' ')*len(attr))
    for s in table:
        for att in attr:
            print('%10s' % (getattr(s, att)), end='')
        print()
'''