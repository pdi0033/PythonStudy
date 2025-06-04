try:
    x = int(input("정수: "))
    y = int(input("정수: "))
    z = x/y
    print(f"x={x}, y={y}, z={z}")
except ZeroDivisionError as e:
    #print(e)    # 에러 메시지를 가져온다.
    print("0으로 나눌 수 없습니다.")
except ValueError as e:
    print("정수를 입력해주세요.")
finally:
    print("에러가 발생하든 말든 이 부분은 반드시 실행된다.")
    # 주로 파일, 데이터베이스, 네트워크 처리 등에 많이 사용한다.
    # 파일, 데이터베이스, 네트워크 연결 .... 오류 발생 close