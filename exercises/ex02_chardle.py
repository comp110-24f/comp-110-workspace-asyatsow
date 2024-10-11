"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730771725"


def input_word() -> str:

    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
    return word


def input_letter() -> str:

    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
    return letter


def contains_char(word: str, letter: str) -> None:

    print("Searching for", letter, "in", word)
    count = 0  # Initialize count of matches

    # Check each index of the word
    for index in range(len(word)):
        if word[index] == letter:
            print(letter, "found at index", index)
            count += 1  # Increment count on a match

    if count == 0:
        print("No instances of", letter, "found in ", word)
    elif count == 1:
        print("1 instance of", letter, "found in ", word)
    else:
        print(count, "instances of", letter, "found in", word)


def main() -> None:

    word = input_word()

    if len(word) != 5:
        return  # if the letter dne it exits

    letter = input_letter()
    # Check if letter is valid before proceeding
    if len(letter) != 1:
        return  # if the letter dne it exits
    contains_char(word, letter)  # Perform the character check


if __name__ == "__main__":
    main()


"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730771725"


def main() -> None:
    """This defines the main function which will all be under all the other functions"""
    word: str = input_word()
    letter = input_letter()
    countains_char(word, letter)


# having to define it b4 using it ^
def input_word() -> str:
    """defines input word"""
    word_response: str = input("Enter a 5-character word:")
    if len(word_response) == 5:
        return word_response
    elif len(word_response) != 5:
        print("Error: Word must contain 5 characters.")
        return word_response
        # conditions for whether or not word response will return


def input_letter() -> str:
    """defines input lettr"""
    letter_response: str = input("Enter a single character: ")
    if len(letter_response) == 1:
        return letter_response

    elif len(letter_response) != 1:
        print("Error: Word must be a single character.")
        return letter_response
        exit()


def contains_char(word: str, letter: str) -> None:
    """defines contain character"""
    print("Searching for" + letter + "in" + word)
    count: int = 0

    if word[0] == letter:
        print(letter + "found at index 0")
        count += 1

        # because we aren't using a while loop we must go through each if statement for all the potential cases

    if word[1] == letter:
        print(letter + "found at index 1")
        count += 1

    if word[2] == letter:
        print(letter + "found at index 2")
        count += 1

    if word[3] == letter:
        print(letter + "found at index 3")
        count += 1

    if word[4] == letter:
        print(letter + "found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + "found in" + word)

    # We had to specify this because of the difference between instance and instances
    elif count == 1:
        print("1 instance of " + letter + "found in" + word)
    else:
        print(str(count) + "instances of" + letter + "found in" + word)


if __name__ == "__main__":
    main()

    """EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730771725"


def main() -> None:
    """This defines the main function which will all be under all the other functions"""
    word: str = input_word()
    letter = input_letter()
    contains_char(word, letter)


# having to define it b4 using it ^
def input_word() -> str:
    """defines input word"""
    word_response: str = input("Enter a 5-character word:")
    if len(word_response) == 5:
        return word_response
    elif len(word_response) != 5:
        print("Error: Word must contain 5 characters.")
        return word_response
        # conditions for whether or not word response will return


def input_letter() -> str:
    """defines input lettr"""
    letter_response: str = input("Enter a single character: ")
    if len(letter_response) == 1:
        return letter_response

    elif len(letter_response) != 1:
        print("Error: Word must be a single character.")
        return letter_response
        exit()


def contains_char(word: str, letter: str) -> None:
    """defines contain character"""
    print("Searching for" + letter + "in" + word)
    count: int = 0

    if word[0] == letter:
        print(letter + "found at index 0")
        count += 1

    # because we aren't using a while loop we must go through each if statement for all the potential cases

    if word[1] == letter:
        print(letter + "found at index 1")
        count += 1

    if word[2] == letter:
        print(letter + "found at index 2")
        count += 1

    if word[3] == letter:
        print(letter + "found at index 3")
        count += 1

    if word[4] == letter:
        print(letter + "found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + "found in" + word)

    # We had to specify this because of the difference between instance and instances
    elif count == 1:
        print("1 instance of " + letter + "found in" + word)
    else:
        print(str(count) + "instances of" + letter + "found in" + word)


if __name__ == "__main__":
    main()
