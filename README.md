# Gunbot Stats Tool
Tool for plotting gunbot buy/sell orders with the price of the index (currency pair).

## Overview
The script is meant to generate a chart of the price history of a given
currency/cryptocurrency pair, and plot all orders (buys/sells) onto a chart.
It takes a Gunbot CSV file as input and fetches price information from the
[Crypto Compare API](https://www.cryptocompare.com/api/#), then it generates
a chart which it outputs in the form of an image.

**Work in progress**

## Python version
Python 3.6

## Configuration
Run `virtualenv -p python3 venv && source venv/bin/activate && pip install -r requirements.txt`

### New dependencies
After installing new dependencies, run `pip freeze > requirements.txt` to persist them.

## Running
`source venv/bin/activate` to activate the virtualenv.<br>
`python3 main.py [fullOrders.csv]` to run the script.
