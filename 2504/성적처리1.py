# 이름, 국어, 영어, 수학 성적을 입력 받아 총점과 평균을 구하여 출력
# 입력: 이름(문자열), 국어, 영어, 수학
# 출력: 총점, 평균

student_name = input("이름? ")
student_kor = int(input("국어? "))
student_eng = int(input("영어? "))
student_mat = int(input("수학? "))

# 계산
score_total = (student_kor + student_eng + student_mat)
score_average = score_total // 3

# 출력
print("총점:", score_total, "  평균:", score_average)