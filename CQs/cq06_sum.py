"""Summing the elements of a list using different loops"""

__author__ = "730771725"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = vals[idx]
    while len(vals) < vals[idx]:
        sum = sum + vals[idx]
    idx += 1
    return sum  # I KEEP FORGETTING THE RETURN LINE


def f_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = vals[idx]
    for values in vals:
        sum = sum + values  # This has to add up values not vals
        # Thats the part I keep getting confused about
    return sum  # I KEEP FORGETTING THE RETURN LINE


def f_range_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = vals[idx]
    for values in range(0, len(vals)):  # This for loop works the same
        # the sum has to equal the first indx indation to what the values are
        sum = sum + values
    return sum  # I KEEP FORGETTING THE RETURN LINE
