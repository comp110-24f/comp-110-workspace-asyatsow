"""Concatenation file"""

__author__ = "730771725"

word1 = "happy"
word2 = "tuesday"

def concat(str1: str, str2: str) -> str: 
    print(str1 + str2)
    return str1 + str2

print(concat(word1, word2))  

# something that you have to remember is 
# that a call function doesnt have to look like 
# concat(word1 = x, word2 = y)/ It can look as simple as line 12 
# because we are still calling it and using the global values established

if __name__ == "__main__":


