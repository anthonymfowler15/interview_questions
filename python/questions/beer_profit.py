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

