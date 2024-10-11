"""Mutating functions."""

__author__ = "730771725"


def manual_append(list: list[int], integer: int) -> None:
    list.append(
        integer
    )  # append means to add a value to the list, which would be the integer


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[
            index
        ] *= 2  # We did not use append because we aren't trying to add something to the list
        # we want at each index for it to multiply it by 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)  # This is me calling the double function

print(list_1)
print(list_2)
