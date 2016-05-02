# Two fermenters
# A B
A = None
B = None

# List key value pairs of bars want different beers
# time is time from 0 that they need the beer by. OK to let them fall through, but they will not pay for the beer after this date.
orders =
    [
	   {"la_brew": { {'kegs': 5}, {'type': 'pilsner'}, {'time': 5}}},
	   {"sf_brewery": { {'kegs': 10}, {'type': 'lambic'}, {'time': 7}}},
	   {"sunnyvale_bar": { {'kegs': 2}, {'type': 'ipa'}, {'time': 3}}}
    ]

# time table:
time_table = {'pilsner': 1, 'ipa': 2, 'lambic': 5}

# profit table:
profit_table = {'pilsner': 5, 'ipa': 15, 'lambic': 10}

# 50 days in a month
DAYS = 50

# how do you maximize profit? What is the maximum profit that we can get from this list of orders?

# Solution
A = { weeks_left: 0 }
B = { weeks_left: 0 }




# Warm up: which order gives us the most profit per week?

# Solution
max_profit = 0
for order in orders:
  money_earned = order['kegs'] * profit_table[order['type']]
  money_per_week = money_earned / time_table[order['type']]
  if money_per_week > max_profit:
    max_profit = money_per_week
print max_profit
