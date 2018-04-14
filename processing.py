import csv

import plotly
import urllib3

from typedefs import Order


def csv_to_orders(csvfile):
    reader = csv.reader([line.replace('\0', '') for line in csvfile])
    # Skip header
    next(reader, None)

    for row in reader:
        # Ignore empty rows
        if not row:
            continue
        yield Order(row)


def handle_orders(orders, **kwargs):
    if kwargs['pairs']:
        pairs = set([order.exchange for order in orders])
        for pair in pairs:
            print(pair)
    elif kwargs['exchange']:
        orders = filter(lambda order: order.exchange == kwargs['exchange'], orders)
        for order in orders:
            print(order)
