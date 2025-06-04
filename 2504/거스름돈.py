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
total_price = 27560 # int(input("물건 값: "))
input_money = 100000 #int(input("지불한 값: "))
remain_money = input_money - total_price
change_money = 50000

if remain_money < 0:
    print("지불한 값이 부족합니다.")
else :
    for i in range(0, 8):
        if i % 2 == 0:
            # 5## 원
            print(f"{change_money}원\t {remain_money // change_money} 장")
            remain_money %= change_money
            change_money = int(change_money/5)
        else:
            # 1## 원
            print(f"{change_money}원\t {remain_money // change_money} 장")
            remain_money %= change_money
            change_money = int(change_money/2)


"""
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
    