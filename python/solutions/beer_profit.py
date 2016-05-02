# Question:
# You own a brewery and wish to maximize profit from bars that want your beer


# List key value pairs of bars want different beers
orders=[
  {'brewery': 'la_brew', 'kegs': 5, 'type': 'pilsner'},
  {'brewery': 'sf_brewery_united', 'kegs': 2, 'type': 'ipa'},
  {'brewery': 'sunnyvale_hipster_bar', 'kegs': 10, 'type': 'lambic'}
]

# time table (time it takes to brew any amount of kegs for a particular beer type):
time_table = {'pilsner': 1, 'ipa': 2, 'lambic': 5}

# profit table(money received per keg of beer):
profit_table = {'pilsner': 5, 'ipa': 15, 'lambic': 10}

# 10 days to work with
DAYS = 7

# =====QUESTION=====
# how do you maximize profit? What is the maximum profit that we can get from this list of orders?
# Assume you can make any number of kegs in an order
# Assume each beer type is only requested once
# =====ENDQUESTION=====

# ======SOLUTION=====
def find_profit(profit, order_queue, orders_taken, days_left):
  if not order_queue:
    return profit, orders_taken

  if days_left < time_table[order_queue[0]['type']]:
    return find_profit(profit, order_queue[1:len(order_queue)], orders_taken, days_left)

  cur_order = order_queue[0]
  proft_from_order = cur_order['kegs'] * profit_table[cur_order['type']]
  days_left_if_take_order = days_left - time_table[cur_order['type']]
  orders_taken_if_take_order = orders_taken + [cur_order]

  order_taken_total, order_taken_list = find_profit(proft_from_order + profit, order_queue[1:len(order_queue)], orders_taken_if_take_order, days_left_if_take_order)

  order_skipped_total, order_skipped_list = find_profit(profit, order_queue[1:len(order_queue)], orders_taken, days_left)

  if order_taken_total > order_skipped_total:
    return order_taken_total, order_taken_list
  else:
    return order_skipped_total, order_skipped_list

profit, orders_taken = find_profit(0, orders, [], DAYS)
print profit
print orders_taken
# =====ENDSOLUTION=====

