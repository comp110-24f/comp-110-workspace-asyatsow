"""Coordinates file"""

__author__ = "730771725"


def get_coords(xs: str, ys: str) -> None:  # first I defined get undercoured
    idx1 = 0  # set the first index = 0
    while idx1 < len(
        xs
    ):  # if the index is less than the length of xs then continue onto the next code
        # idx1 += 1 # this cannot be here because if you did put it here it would skip the first character of xs.
        # This should be done after completing the nested while loop
        idx2 = 0
        while idx2 < len(ys):
            # idx2 +=1 cannot be here you incremented it before
            # acessing ys
            print(xs[idx1], ys[idx2])
            idx2 += 1
        idx1 += 1  # this has to be after or else it wont print out the
        # first character in xs
