def solution(s):
    answer = ''
    isFirst = True
    for ch in s:
        if ch == " ":
            isFirst = True
        elif isFirst == True:
            if ch.isalpha() == True:
                ch = ch.upper()
            isFirst = False
        elif ch.isalpha() == True:
            ch = ch.lower()
        answer += ch
    return answer

print(solution(	"whY am  i     cRY1ing"))
print("Why Am  I     Cry1ing")