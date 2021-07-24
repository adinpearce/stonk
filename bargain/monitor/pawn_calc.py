def calc(price):
    handling = (price * 1000) * 0.00321
    profit = (price * 1000) * 0.02

    total_fee = (profit + handling) / 1000
    return_fee_long = round(total_fee + price, 2)

    return_fee_short = round(price - total_fee, 2)

    return return_fee_long, return_fee_short

#print(calc(213.5))
