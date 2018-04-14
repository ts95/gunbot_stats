#!/bin/python3

import sys
import argparse
import csv

import processing

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', type=str, help="Gunbot CSV file")
    parser.add_argument('-e', '--exchange', type=str, help="Currency pair. E.g. BTC-ETH")
    parser.add_argument('-p', '--pairs', action='store_true', help="Print all the currency pairs in the CSV file")

    args = parser.parse_args()

    if str(args.csv).endswith('.csv') and (args.exchange or args.pairs):
        with open(args.csv, newline='') as csvfile:
            orders = processing.csv_to_orders(csvfile)
            processing.handle_orders(orders, exchange=args.exchange, pairs=args.pairs)
    else:
        parser.print_help()


if __name__ == '__main__':
    def is_venv():
        return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

    if sys.version_info < (3, 6):
        raise Exception("This script requires Python 3.6 or higher.")

    if not is_venv():
        raise Exception("Activate venv before running the script. `source venv/bin/activate`")

    main()
