import math

def isPalindrom(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False

def isPalindrom2(word: str) -> bool:
    ln = len(word)
    for i in range(0, ln//2):
        if word[i] != word[ln-i-1]:
            return False
    return True


word = "racecar"
print(isPalindrom(word))
print(isPalindrom2(word))

