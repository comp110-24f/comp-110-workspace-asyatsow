__author__ = "730771725"


def mimic(message: str) -> str:
    """The purpose is to define message as a string"""
    return message


def main() -> None:
    """Saying that the main has no parameter so its not going to return anything"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
