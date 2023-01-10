import csv

class BasePipeline:
  
    def __init__(self, file, parsers, delimiter=','):
        self.file = file
        self.parsers = parsers
        self.delimiter = delimiter

    def __call__(self):
        with open(self.file) as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                print(self.parsers[0](row))

class CSVPipeline(BasePipeline):
    pass

class OneLinePipeline(BasePipeline):

    def __call__(self):
        with open(self.file) as infile:
            reader = csv.DictReader(infile)

            print(self.delimiter.join(str(self.parsers[0](row)) for row in list(reader)[:10]))