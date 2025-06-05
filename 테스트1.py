def solution(numbers):
    answer = 0
    strArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, value in enumerate(strArr):
        numbers = numbers.replace(value, str(index))
    print(answer)
    return (answer)

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
print(solution("oneonetwotwothreethree"))
print(solution("onetwoonezerozeroninefivenine"))
