# 이름 국어 영어 수학 총점 평균
# 평균에 대해서 수(90) 우(80) 미(70) 양(60) 가(60미만)
# 3명
# 딕셔너리 형식
studentList = []

# 입력
for i in range(0,3):
    student = {}
    student["name"] = input("이름: ")
    student["korean"] = int(input("국어: "))
    student["english"] = int(input("영어: "))
    student["math"] = int(input("수학: "))
    studentList.append(student)

# 계산
for student in studentList:
    student["total"] = student["korean"] + student["english"] + student["math"]
    student["average"] = student["total"] / 3

for student in studentList:
    score = ""
    if student["average"] >= 90:
        score = "수"
    elif student["average"] >= 80:
        score = "우"
    elif student["average"] >= 70:
        score = "미"
    elif student["average"] >= 60:
        score = "양"
    else:
        score = "가"

    student["score"] = score

# 출력
for student in studentList:
    print(f"{student["name"]}", end = "\t")
    print(f"{student["korean"]}", end = "\t")
    print(f"{student["english"]}", end = "\t")
    print(f"{student["math"]}", end = "\t")
    print(f"{student["total"]}", end = "\t")
    print(f"{student["average"]:.2f}", end = "\t")
    print(f"{student["score"]}")
