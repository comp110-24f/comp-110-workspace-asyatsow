"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730771725"


def main() -> None:
    """This defines the main function which will all be under all the other functions"""
    word: str = input_word()
    letter: str = input_letter()
    contains_char(word, letter)


# having to define it b4 using it ^
def input_word() -> str:
    """defines input word"""
    word_response: str = input("Enter a 5-character word: ")
    if len(word_response) > 5 or len(word_response) < 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Exit if the word is not 5 characters

    else:
        print(word_response)
    return word_response


def input_letter() -> str:
    """defines input letter"""
    letter_response: str = input("Enter a single character: ")
    if len(letter_response) < 1 or len(letter_response) > 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print(
            letter_response
        )  # This is where I kept making a mistake. It must both PRINT and RETURN a value. I understand the diffference btwn the two
    return letter_response


def contains_char(word: str, letter: str) -> None:
    """defines contain character which has the parameters word and letter"""
    print("Searching for " + letter + " in " + word)
    count: int = 0  # initalizing count

    if (
        word[0] == letter
    ):  # going through all of the potential index numbers it can have
        print(letter + " found at index 0")
        count += 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # this is important because 1 count cannot have an s at the end
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
