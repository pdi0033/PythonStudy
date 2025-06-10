def getTempList(st, isExp = False):
    strList = st.split(' ')
    mList = []
    oStr = ""
    for s in strList:
        if s.isdigit():
            num = int(s)
            mTuple = []
            while num > 0:
                mTuple.append(num%10)
                num = num//10
            mList.append(mTuple)
        elif s in "+-":
            oStr = s
    #print("mList: ", mList, oStr)
    temp = [0] * max(len(x) for x in mList)
    for value in range(0, len(mList)):
        if value == 0:
            for i, m in enumerate(mList[value]):
                temp[i] += m
        elif value == 1:
            for i, m in enumerate(mList[value]):
                if oStr == "+":
                    temp[i] += m
                elif oStr == "-":
                    temp[i] -= m
        elif value == 2 and isExp == True:
            for i, m in enumerate(mList[value]):
                temp[i] -= m

    return temp

def solution1(expressions):
    answer = []
    bCorrect = False
    n = set(range(2,10))      # 2~9 진법
    res = [x for x in expressions if 'X' in x]
    exp = [x for x in expressions if 'X' not in x]
    # 진법은 1의 자리수보다 크다.
    for st in expressions:
        strList = st.split(' ')
        digitList = [x for x in strList if x.isdigit()]
        for d in digitList:
            num = max(int(c) for c in d)
            n = (x for x in n if x > num)
        #     if num >= n:
        #         n = num + 1
        #         if n == 9:
        #             bCorrect = True
        #             break
        # if bCorrect == True:
        #     break
                
    if bCorrect == False:
        for st in exp:
            temp = getTempList(st, isExp=True)
            #print(temp)
            if not any(temp):
                continue

            one = (-1) * temp[0]
            for i in range(n, 9+1):  # 쌩으로 2에서 9 대입해서 찾기
                x = 0
                for index, value in enumerate(temp):
                    if index != 0:
                        x += value * i ** (index)
                if x == one:
                    bCorrect = True
                    n = i
                    break
            print(n, bCorrect)
            if bCorrect:
                break
    
    if bCorrect == True:
        for st in res:
            temp = getTempList(st, isExp=False)

            x = 0
            for index, value in enumerate(temp):
                x += value * n ** (index)
            ans = ""
            while x > 0:
                ans = str(x%n) + ans
                x = x // n
            #print("res: ",temp, "a: ", x, "ans: ", ans)
            st = st.replace('X', ans)
            print(st)
            answer.append(st)
    else:       # 답을 확실히 구하지 못했을 때
        for st in res:
            temp = getTempList(st, isExp=False)
            ans = ""
            for index, value in enumerate(temp):
                if value >= n or value < 0:
                    ans = "?"
                    break
                else:
                    ans = str(value) + ans
            
            print("res: ", temp, "n: ", n, "ans: ", ans)
            st = st.replace('X', ans)
            print(st)
            answer.append(st)
    
    
    return answer





def solution(expressions):
    answer = []
    print(expressions)
    n = set(range(2,10))      # 2~9 진법
    res = [x for x in expressions if 'X' in x]
    exp = [x for x in expressions if 'X' not in x]
    # 각 자리수 확인하여 진법 후보 좁히기 
    for st in expressions:
        strList = st.split(' ')
        digitList = [x for x in strList if x.isdigit()]
        for d in digitList:
            num = max(int(c) for c in d)
            n = {x for x in n if x > num}

    print(n)
    for st in exp:
        temp = getTempList(st, isExp=True)
        if not any(temp):
            continue

        one = (-1) * temp[0]
        valid_bases = set()
        for i in n:  # 쌩으로 2에서 9 대입해서 찾기
            x = 0
            for index, value in enumerate(temp):
                if index != 0:
                    x += value * i ** (index)
            if x == one:
                valid_bases.add(i)
        n = n.intersection(valid_bases)
        print(n)

    for st in res:
        temp = getTempList(st, isExp=False)
        results = set()

        for i in n:  # 쌩으로 2에서 9 대입해서 찾기
            x = 0
            for index, value in enumerate(temp):
                x += value * i ** (index)
            if x == 0:
                results.add('0')
            else:
                ans = ""
                while x > 0:
                    ans = str(x%i) + ans
                    x = x // i
                results.add(ans)
        if len(results) == 1:
            st = st.replace('X', results.pop())
        else:
            st = st.replace('X', '?')
        print(st)
        answer.append(st)
    
    
    return answer

# print("answer= ",solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# print()
# print("answer= ",solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print()
# print("answer= ",solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print()
print("answer= ",solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
print()
# print("answer= ",solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
# print()
# print("answer= ",solution(["13 + 4 = X", "24 - 5 = X", "16 + 3 = X"]))
# print()



