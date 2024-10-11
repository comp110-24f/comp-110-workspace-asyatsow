""" Wordle expansion ex03 assignment"""

__author__ = "730771725"


def input_guess(correct_word_length: int) -> str:
    """Prompts user for a guess of a specific length until a valid guess is received."""
    while True:  # Infinite loop until a valid guess is provided
        guessed_word: str = input(f"Enter a {correct_word_length} character word: ")
        if len(guessed_word) != correct_word_length:
            print(f"That wasn't {correct_word_length} chars! Try again: ")
        else:
            return guessed_word  # Return the valid guessed word


def contains_char(secret_word: str, single_char_guess: str) -> bool:
    """We defined contains char, and set the parameters for it to return either a True or False"""
    assert len(single_char_guess) == 1
    return (
        single_char_guess in secret_word
    )  # Check if the character is in the secret word


# However, it has to return the boolean of the entire function instead of
# simply the single character guess because thats how we will know if it
# is True or False. It will return None for bool of single_char_guess bcuz
# you can't ask whether its true or false for a character. It wont return anything


def emojified(user_guess: str, secret_word: str) -> str:
    """Defined emojified, parameters = user's guess and secret word, returning a string"""
    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"  # White box emoji
    GREEN_BOX: str = "\U0001F7E9"  # Green box emoji
    YELLOW_BOX: str = "\U0001F7E8"  # Yellow box emoji

    result = ""

    index = 0

    while index < len(
        user_guess
    ):  # This statement needs to be used in order to run all of the if, elif, and else statements
        if (
            user_guess[index] == secret_word[index]
        ):  # At that specific index it will run the code
            result += GREEN_BOX  # Add green box for correct character
        elif contains_char(
            secret_word, user_guess[index]
        ):  # Check if the character is in the secret word
            result += (
                YELLOW_BOX  # Add yellow box for correct character in the wrong position
            )
        else:
            result += WHITE_BOX  # Add white box for incorrect character
        index += 1  # Increment index

    return result  # Return the emoji result string


def main(secret_word: str) -> None:
    turns_played: int = 0
    max_turns: int = 6
    won: bool = (
        False  # If this is false, I want you to run it as False because it will stop the program
    )

    while turns_played < max_turns and not won:
        print(
            f"=== Turn {turns_played + 1}/{max_turns} ==="
        )  # Printing the number of times played
        guess: str = input_guess(len(secret_word))  # Get a valid guess from the player
        result: str = emojified(
            guess, secret_word
        )  # Get the emoji result for the guess
        print(result)  # Print the emoji result

        if guess == secret_word:  # Check if the guess is correct
            won = True  # Set the won flag to True

        turns_played += 1  # Increment the number of turns played

    if won:
        print(f"You won in {turns_played}/{max_turns} turns!")
    else:
        print(
            f"X/{max_turns} - Sorry, try again tomorrow!"
        )  # Message for losing the game


if __name__ == "__main__":
    main(secret_word="codes")
