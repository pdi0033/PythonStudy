try:
    a = [1,2,3,4,5]
    b = a[5]
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:  # 폭포수(casecading)
    print(e)


class Test:
    def __init__(self):
        #return True
        raise Exception("객체 생성오류")
    

try:
    t1 = Test()
except Exception as e:
    print(e)