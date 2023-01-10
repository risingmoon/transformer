#!/usr/bin/env python3
import argparse

from transformer.pipeline import CSVPipeline, OneLinePipeline
from transformer.parser import get_parsers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-p', '--parsers', action='append')
    parser.add_argument('-c', '--config')
    parser.add_argument('--oneline', action='store_true')
    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r') as config:
            parsers = get_parsers(config.readlines())
    else:
        parsers = get_parsers(args.parsers)

    if args.oneline:
        OneLinePipeline(args.file, parsers)()
    else:
        CSVPipeline(args.file, parsers)()


if __name__ == '__main__':
    main()