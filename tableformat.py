# Exercise 3.2

def print_table(table, attr):
    for att in attr:
        print('%10s' % (att), end='')
    print()
    print(('-'*10 + ' ')*len(attr))
    for s in table:
        for att in attr:
            print('%10s' % (getattr(s, att)), end='')
        print()