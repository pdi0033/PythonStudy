from 괄호짝맞추기 import MyStack

"""
피연산자(숫자)는 스택에 넣는다. 그럼, 스택의 상태는 [3, 5, 2]이다.
연산자를 만나면 스택에서 피연산자 두 개를 꺼내서 계산한다.
연산자 *를 만났으므로 스택에서 2와 5를 꺼내서 곱한다. 5 * 2 = 10
결괏값을 스택에 저장한다. 이제 스택의 상태는 [3, 10]다.
그다음에 연산자 +가 있으므로 스택에서 10과 3을 꺼내서 더한다. 답은 13이다.
"""

def postFix(str):
    dataList = []
    opList = "+-/*"
    postStr = ""
    for s in str:
        if s not in opList:
            postStr += s

    return postStr

def postResult(str):
    dataList = []
    opList = "+=/*"
    str = str.strip()
    for s in str:
        if s not in opList:
            dataList.append(int(s))
        else:
            right = dataList.pop()
            left = dataList.pop()
            x = 0
            if s == "+":
                x = left + right
            elif s == "-":
                x = left - right
            elif s == "*":
                x = left * right
            elif s == "/":
                x = left / right
            dataList.append(x)
    return dataList

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

# 수식을 받아가서 연산 결과를 반환해야 한다.
def postResult2(postfix):
    stack = MyStack(100)
    for c in postfix:
        if isDigit(c):
            stack.push(c)
        elif isOperator(c):
            right = stack.pop()
            left = stack.pop()
            result = operate(c, left, right)
            stack.push(result)
    return stack.pop()


if __name__ == "__main__":
    str1 = "3+5*2"
    str2 = "3*5+2"
    answer1 = "352*+"
    answer2 = "35*2+"
    
    print(postResult(answer1))
    print(postResult(answer2))

    s = "4 5 2 * + 7 3 / -"
    print(postResult2(s))

