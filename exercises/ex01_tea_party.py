"""Using python to perform small math (Teabags)"""

__author__: str = "730771725"


def main_planner(guests: int) -> None:
    """defines main planner and turns nothing"""
    print("A Cozy Tea Party for " + str(guests), "People!")

    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # this part makes no sense to me I inputted values that cannot change
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """defining tea bags and stating that people is an int and the return type should be an int"""
    return people * 2
    # we didn't call the function here we do that in the trail head so you are asking it to return whatever number of people and multiply it by 2


def treats(people: int) -> int:
    """This uses a different paramaeter with a different parameter people but returning an int as well"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This is defining cost with the paramaters of tea and treat count and returning a float"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
