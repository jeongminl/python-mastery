def parse_line(input_string):
    if '=' not in input_string:
        return None
    return tuple(input_string.split('='))