__author__: str = "730771725"


def guess_a_number() -> None:
    secret: int = 7

    guess_a_number = int(input("Guess a number:"))
    print("Your guess was", guess_a_number)

    if guess_a_number == secret:
        print("You got it!")
    if guess_a_number < secret:
        print("Your guess was too low! The secret number is", secret)
    if guess_a_number > secret:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
