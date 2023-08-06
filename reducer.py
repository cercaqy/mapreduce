#!/usr/bin/env python
"""reducer.py"""

import sys


def perform_reduce():

    full_payment_type = {
        1: 'Credit card',
        2: 'Cash',
        3: 'No charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided trip'
    }

    current_month = None
    current_sum = [0] * len(full_payment_type)
    current_count = [0] * len(full_payment_type)
    tips_avg_amount = [0] * len(full_payment_type)

    print("Month,Payment type,Tips average amount")

    for line in sys.stdin:
        line = line.strip()
        month, payment_type, tip_amount = line.split(',')

        payment_type = int(payment_type)
        tip_amount = float(tip_amount)


        if month == current_month:
            current_sum[payment_type - 1] += tip_amount
            current_count[payment_type - 1] += 1
        else:
            if current_month:
                for j in range(len(full_payment_type)):
                    if current_count[j]:
                        tips_avg_amount[j] = current_sum[j] / current_count[j]
                        print('%s,%s,%s' % (current_month, full_payment_type[j + 1], tips_avg_amount[j]))

            current_month = month
            current_sum = [0] * len(full_payment_type)
            current_count = [0] * len(full_payment_type)
            current_sum[payment_type - 1] += tip_amount
            current_count[payment_type - 1] += 1

    for j in range(len(full_payment_type)):
        if current_count[j]:
            tips_avg_amount[j] = current_sum[j] / current_count[j]
            print('%s,%s,%s' % (current_month, full_payment_type[j + 1], tips_avg_amount[j]))

if __name__ == '__main__':
    perform_reduce()