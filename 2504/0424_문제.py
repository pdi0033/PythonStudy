"""
# 문제1) m를 km와 m로 전환하기.
# 2300 미터는 2km와 300미터 입니다.
# 미터를 입력받아서 각각 km와 m로 전환해서 출력하세요.
# 힌트) 몫 구하는 연산자 //, 나머지 구하는 연산자 %
input_m = int(input("몇 m 입니까? "))
trans_km = input_m // 1000
trans_m = input_m % 1000
print(f"{input_m}m는 {trans_km}km {trans_m}m 입니다. \n")
"""

"""
# 문제2) 사다리꼴이 면적 구하기  
# 사다리꼴 면적 : (윗변 + 아랫변) * 높이 /2   
print("사다리꼴 면적을 구합니다.")
up_length = int(input("윗변: "))
down_length = int(input("아랫변: "))
height = int(input("높이: "))
area = (up_length + down_length) * height / 2
print(f"사다리꼴의 면적은 {area}입니다. \n")
"""


"""
# 문제3) 철수가 식료품점에 가서 과일을 샀다 사과와 배를 샀는데 사과는 
#       한개에 5000 원이고 배는 10000원이다. 각각 사과와 배의 개수를 
#       입력받아 총금액을 구하는 프로그램을 작성하시오
print("철수가 산 사과와 배의 총금액을 구합니다.")
apple_price = 5000
pear_price = 10000
apple_count = int(input("사과의 개수: "))
pear_count = int(input("배의 개수: "))
total_price = apple_count * apple_price + pear_count * pear_price
print(f"총 금액은 {total_price}원 입니다. \n")
"""


"""
# 문제4) 거스름돈 계산하기 - 10만원 짜리 넣고 거스름돈 받기
# 물건값이 총 : 27560 원
# 거스름돈 : 72440 원
#   50000 -- 1 장 
#   10000 -- 2 장 
#    5000 -- 0 장
#    1000 -- 2 장
#     500 -- 0 개 
#     100 -- 4 개
#      50 -- 0 개
#      10 -- 4개
print("10만원을 내고 거스름돈을 계산합니다.")
total_price = int(input("물건 값: "))
input_money = 100000 #int(input("지불한 값: "))
remain_money = input_money - total_price
if remain_money < 0:
    print("지불한 값이 부족합니다.")
else :
    # 선생님께선 전부 변수를 만들라고 하셨지만.......
    # 초보자의 초반 버릇을 위해 그런 것이라 믿고 이렇게 쓰겠습니다.....
    # 한 번만 봐주세요...
    print(f"거스름 돈을 드립니다.")
    print(f"[지폐]")
    print(f"50000원 {remain_money // 50000}장")
    remain_money = remain_money % 50000
    print(f"10000원 {remain_money // 10000}장")
    remain_money = remain_money % 10000
    print(f"5000원 {remain_money // 5000}장")
    remain_money = remain_money % 5000
    print(f"1000원 {remain_money // 1000}장")
    remain_money = remain_money % 1000

    print(f"[동전]")
    print(f"500원 {remain_money // 500}개")
    remain_money = remain_money % 500
    print(f"100원 {remain_money // 100}개")
    remain_money = remain_money % 100
    print(f"50원 {remain_money // 50}개")
    remain_money = remain_money % 50
    print(f"10원 {remain_money // 10}개")
    print(f"")
"""

# 문제5) 문자열 연습하기
# 5-1. 변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
names = "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
print(names, type(names))

# 5-2. => list 타입으로 전환해서
names = names.split(",")
print(names, type(names), len(names))

# 인덱싱    list, string 경우에 각 요소를 숫자를 통해서 접근 가능하다
# 0,1,2,3,4,...
# 슬라이싱  [시작값:종료값:증감치] 각각 생략 가능하다
# print(names[3:])  # 3번째 이후로 출력
# print(names[:3])  # 0부터 3번째 직전까지 출력
# print(names[::-1])    # 역순
# print(names[2:5])     # 2,3,4 번째 요소만 출력

# 5-3. => "서희"가 몇 번째에 있는지
idx = names.index("서희")
print(f"\'서희\'는 {idx}번째에 있습니다.")

# 5-4. "이순신", "장영실" 존재 여부 확인
if names.count("이순신") > 0 :
    print("\'이순신\'은 있습니다.")
else:
    print("\'이순신\'은 없습니다.")

if "장영실" in names :
    print("\'장영실\'은 있습니다.")
else:
    print("\'장영실\'은 없습니다.")

# 5-5. 추가할 사람: "정도전", "정약용", "최치원", ...
# names.append("정도전")
# names.append("정약용")
# names.append("최치원")
names.extend(["정도전", "정약용", "최치원"])
print(names)

# 5-6. "서희" => "김종서"로 바꾸기
idx = names.index("서희")
names[idx] = "김종서"
print(names)

# 5-7. 장길산 => 김길산 첫 글자만 바꾸기
idx = names.index("장길산")
names[idx] = names[idx].replace("장", "김")
print(names)