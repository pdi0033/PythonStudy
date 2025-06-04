def isEven(n):
    if n%2 == 0:
        return True
    return False

def toUpper(s):
    #A - 65     a - 97
    #32만큼 차이가 남. 소문자를 대문자로-32, 대문자를 소문자로 +32
    us = ""
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            #i = chr(ord(i) - ord('a') + ord('A'))
            i = chr(ord(i)-32)
        us += i
    return us