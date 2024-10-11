# order = docstring,import, then author
"""Visualize file"""
from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

__author__ = "730771725"

x = "123"
y = "abc"

# The reason you were stuck is because you were trying to call concat without definening it
# under anothr variable. Python doesn;t allow you to simply call it with no other variable like
# result attached to it
result = concat(x, y)
print(result)

get_coords(x, y)
