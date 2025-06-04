# 이름 국어 영어 수학 총점 평균
# 평균에 대해서 수(90) 우(80) 미(70) 양(60) 가(60미만)
# 3명
# 리스트 형식
name_list = []
korean_list = []
english_list = []
math_list = []
total_list = []
average_list = []
score_list = []

# 입력
for i in range(0,3):
    name = input("이름: ")
    korean = int(input("국어: "))
    english = int(input("영어: "))
    math = int(input("수학: "))

    name_list.append(name)
    korean_list.append(korean)
    english_list.append(english)
    math_list.append(math)

# 계산
for i in range(len(name_list)):
    total = korean_list[i] + english_list[i] + math_list[i]
    average = total / 3

    total_list.append(total)
    average_list.append(average)

for i in range(len(name_list)):
    score = ""
    if average_list[i] >= 90:
        score = "수"
    elif average_list[i] >= 80:
        score = "우"
    elif average_list[i] >= 70:
        score = "미"
    elif average_list[i] >= 60:
        score = "양"
    else:
        score = "가"

    score_list.append(score)

# 출력
for i in range(len(name_list)):
    print(f"{name_list[i]}",    end="\t")
    print(f"{korean_list[i]}",  end="\t")
    print(f"{english_list[i]}", end="\t")
    print(f"{math_list[i]}",    end="\t")
    print(f"{total_list[i]}",   end="\t")
    print(f"{average_list[i]:.2f}", end="\t")
    print(f"{score_list[i]}")