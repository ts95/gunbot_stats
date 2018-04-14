#!/bin/python3

import argparse
import csv
import io
from datetime import datetime

import plotly
import urllib3

from typedefs import Order

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, help="Gunbot CSV file")

    args = parser.parse_args()

    if str(args.csv).endswith('.csv'):
        with open(args.csv, newline='') as csvfile:
            orders = csv_to_orders(csvfile)
            handle_orders(orders)
    else:
        parser.print_help()


def csv_to_orders(csvfile):
    reader = csv.reader([line.replace('\0', '') for line in csvfile])
    # Skip header
    next(reader, None)

    for row in reader:
        # Ignore empty rows
        if not row:
            continue
        yield Order(row)

def handle_orders(orders):
    print(orders)

if __name__ == '__main__':
    main()
