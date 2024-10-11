__author__: str = "730771725"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index_number: int = 0

    while index_number < len(phrase):
        if phrase[index_number] == search_char:
            count += 1
        index_number += 1

    return count
