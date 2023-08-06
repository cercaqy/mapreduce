#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime

def perform_map():
    columns_count = 18
    for line in sys.stdin:

        line = line.strip()
        values = line.split(',')

        if len(values) != columns_count:
            continue

        tpep_pickup_datetime = values[1]
        payment_type = values[9]
        tip_amount = values[13]

        try:
            tpep_pickup_datetime = datetime.strptime(tpep_pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
            payment_type = int(payment_type)
            tip_amount = float(tip_amount)
        except:
            continue

        if tpep_pickup_datetime[:4] != '2020' or payment_type not in range(1, 7):
            continue

        print('%s,%s,%s' % (tpep_pickup_datetime, payment_type, tip_amount))


if __name__ == '__main__':
    perform_map()