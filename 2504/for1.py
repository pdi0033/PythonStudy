# 반복문
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# range(시작값, 종료값, 증감치) - 시작값부터 시작해서 종료값-1까지 증감치를 가지고 생성해낸다.
print(range(1,11))  # 이건 출력에 'range(1, 11)' 그대로 출력된다.

a = list(range(1,11))
print(a)


for kk in range(2, 100, 2):
    print(kk, end= " ")
print()

for kk in range(98, 1, -2):
    print(kk, end= " ")
print()

# 문제1. 1 2 3 4 5 6 7 8 9 10
#       11 12 13 14 15 16 17 ...
for i in range(1,101):
    print("%2d" % i, end = " ")
    if i % 10 == 0:
        print()

# 문자의 unicode => ord(문자)
print(ord('A'))     # 65
print(ord('B'))     # 66
print(ord('a'))     # 97
print(ord('0'))     # 48
print(ord('1'))     # 49

# 코드값 => 문자로 chr(코드값)
print(chr(49))
print(chr(65))

# for문을 써서 알파벳 A~Z까지 출력하기
for a in range(ord('A'), ord('Z')+1):
    print(chr(a), end = " ")
print()

# 키보드로부터 문장을 입력받아서 각 문자의 개수를 구한다
# 대소문자 무시
# A ===> 5
# B ===> 0

#입력
text = input("문장을 입력하세요. > ")
text = text.upper()

count_alpha = []
for i in range(ord('A'), ord('Z') + 1):
    count_alpha.append(0)

# 계산
for i in text:
    if i.isalpha():
        idx = ord(i) - ord('A')
        count_alpha[idx] += 1
    
# 출력
for i in range(0,len(count_alpha)):
    alpha = chr(i + ord('A'))
    if count_alpha[i] > 0:
        print(f"{alpha}의 개수는 {count_alpha[i]}개 입니다.")


# dict 타입으로 해보기
count_dic = {}  # count_dict()
for i in text:
    if i.isalpha():
        if i in count_dic.keys():
            count_dic[i] += 1
        else:
            count_dic[i] = 1

# for item in count_dic.items():
#     print(item)

# 알파벳 순서대로 출력하기 위해
key_list = list(count_dic.keys())
key_list.sort()

for key in key_list:
    print(f"{key} ==> {count_dic[key]}")