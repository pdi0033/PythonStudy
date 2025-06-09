from stack import MyStack

# 한 글자 받아가서 숫자인지 확인하는 함수
def isDigit(ch):
    if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        return True
    return False

# 연산자인지 확인하는 함수
def isOperator(ch):
    if ch == "+" or ch == "-" or ch == "*" or ch =="/":
        return True
    return False

def operate(c, left, right):
    if c == "+":
        result = int(left) + int(right)
    elif c == "-":
        result = int(left) - int(right)
    elif c == "*":
        result = int(left) * int(right)
    elif c == "/":
        result = int(left) / int(right)
    return result

def isLowPriority(front, ch):
    if (front == '*' or front == '/') \
    and (ch == '+' or ch == '-'):
        return True
    return False

def postResult(str):
    result = ""
    operStack = MyStack(len(str)/2)
    for s in str:
        if isDigit(s):
            result += s + " "
        elif isOperator(s):
            front = operStack.peek()
            if isLowPriority(front, s):
                while not operStack.isEmpty():
                    o = operStack.pop()
                    result += o + " "
            operStack.push(s)

    while not operStack.isEmpty():
        o = operStack.pop()
        result += o + " "
    return result


if __name__ == "__main__":
    str1 = "3+5*2"
    str2 = "3*5+2"
    answer1 = "352*+"
    answer2 = "35*2+"
    
    print(postResult(str1))
    print(postResult(str2))

    s = "4 5 2 * + 7 3 / -"
    #print(postResult2(s))