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


# NOTES
# This question tests recursion and parsing of data


# Variation 2
# Assume you can make any number of kegs at a time for a particular type of beer
# Each beer type can be requested more than once


# Variation 3
# Breweries need to have the beer by x days after 0
# After that time, you cannot fulfill the request
orders=[
  {'brewery': 'la_brew', 'kegs': 5, 'type': 'pilsner', 'time': 2},
  {'brewery': 'sf_brewery_united', 'kegs': 2, 'type': 'ipa', 'time': 2},
  {'brewery': 'sunnyvale_hipster_bar', 'kegs': 10, 'type': 'lambic', 'time': 2}
]

time_table = {'pilsner': 1, 'ipa': 2, 'lambic': 3}









