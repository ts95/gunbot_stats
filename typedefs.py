from datetime import datetime

class Order:

    def __init__(self, csv_row):
        date_format = '%m/%d/%Y %I:%M:%S %p'

        self.uuid = csv_row[0]
        self.exchange = csv_row[1]
        self.type = csv_row[2]
        self.quantity = float(csv_row[3])
        self.limit = float(csv_row[4])
        self.comission_paid = float(csv_row[5])
        self.price = float(csv_row[6])
        self.opened = datetime.strptime(csv_row[7], date_format)
        self.closed = datetime.strptime(csv_row[8], date_format)
