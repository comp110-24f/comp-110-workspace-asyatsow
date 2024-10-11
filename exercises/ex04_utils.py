"""EX04 Lists Assignment"""

__author__ = "730771725"

# the function all should return a boolean whether all of the integers,
# in the list are the same as the given int


def all(list: list[int], integer: int) -> bool:
    """all function"""
    # if list == integer:
    # return True
    # else:
    # return False
    """This mistake I made ^ was that it wasn't going to be able to go through the entire
    list, so I had to use a while loop"""
    idx: int = 0
    if len(list) == 0:
        return False
    while idx < len(
        list
    ):  # I KEEP WRITING MY WHILE STATEMENTS IN THE OPPOSITE WAY! REVIEW!!
        if list[idx] != integer:
            return False
        idx += 1
    return True


def max(lists: list[int]) -> int:
    """max function"""
    if len(lists) == 0:
        raise ValueError("max() arg is an empty List")
    # ^ We have to remember that lists have indexes starting at 0
    # if there is nothing in there than we know that it should return error
    idx: int = 0
    largest_number = lists[idx]
    while idx < len(lists):
        if largest_number < lists[idx]:
            largest_number = lists[idx]
        idx += 1  # if this was outside of my while loop, it would be an infitnite loop
    return largest_number  # i forgot this part of the instructions

    # took a little long to figure out, but we are using a while loop so it can go through all of the items i nthe list
    # we first placed largest number at the first index and said that if we go through the entire list and we said that if the first value is less than the next index
    # then it needs to be updated to be hte largest value, and we continuously increase the index


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """is_equal function"""
    if len(list1) != len(list2):
        return False

    # if list1[idx1] != list2[idx2]:
    #     return False
    #     print("False")
    idx = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(list: list[int], list2: list[int]) -> None:
    idx = 0
    while idx < len(list2):
        list.append(list2[idx])  # this will append each element from list2 onto list
        idx += 1
