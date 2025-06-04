# 컴퓨터활용능력 시험
# 이름, 필기(400), 워드(200), 스프레드시트(200), 프리젠테이션(200)
# 총점을 구하고 등급 800이상 A, 800미만 600이상 B, 600미만 400이상 C, 400미만 D와 재미험 요망

# 입력
name = input("이름: ")
test_write = -1
test_word = -1
test_spread = -1
test_ppt = -1

while test_write < 0 or test_write > 400 :
    test_write = input("필기: ")
    if not test_write.isdigit():
        test_write = -1
        continue
    test_write = int(test_write)


while test_word < 0 or test_word > 200 :
    test_word = input("워드: ")
    if not test_word.isdigit():
        test_word = -1
        continue
    test_word = int(test_word)


while test_spread < 0 or test_spread > 200 :
    test_spread = input("스프레드시트: ")
    if not test_spread.isdigit():
        test_spread = -1
        continue
    test_spread = int(test_spread)


while test_ppt < 0 or test_ppt > 200 :
    test_ppt = input("프레젠테이션: ")
    if not test_ppt.isdigit():
        test_ppt = -1
        continue
    test_ppt = int(test_ppt)


# 계산
test_total = test_write + test_word + test_spread + test_ppt

if test_total >= 800:
    grade = "성적: A"
elif test_total >= 600:
    grade = "성적: B"
elif test_total >= 400:
    grade = "성적: C"
else:
    grade = "성적: D, 재시험 요망"

# 출력
print()
text = (
    f"이름: {name} \n"
    f"필기: {test_write} \n"
    f"워드: {test_word} \n"
    f"스프레드시트: {test_spread} \n"
    f"프리젠테이션: {test_ppt} \n"
    f"총점: {test_total} \n"
    f"{grade}"
)

print(text)


# 코드 깎는 노인
# 깡... 깡... 깡...