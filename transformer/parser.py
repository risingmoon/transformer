import json

class DataParser:

    def __init__(self, key):
        self.keys = key.split('.') 

    def __call__(self, data):
        for key in self.keys:
            data = data[key]
        return data 

class JsonParser:

    def __init__(self, column, field):
        self.column = column
        self.parser = DataParser(field)

    def __call__(self, row):
        data = json.loads(row[self.column])
        return self.parser(data)

parser_types = {
    'json': JsonParser,
}

def get_parsers(args):
    parsers = []
    for arg in args:
        parser_type, column, field = arg.split(':')
        parsers.append(parser_types[parser_type](column, field))
    return parsers