# escape 문자. 
# \n - 줄바꿈
s = "I like star.\nred star.\nblue star."
print(s)

# \t - 탭
s = "apple\tpear\tbanana"
print(s)

# \\ 혹은 문자열 앞에 r을 붙인다.- 역슬래시
s = "C:\\User\\temp"
sr = r"C:\User\temp"
print(s)
print(sr)

# 문장 안에 '나 "가 있을 때 처리 방식
# \' \"
s = "I like \'stepany\'"
print(s)
s = "I like \"stepany\""
print(s)

# print() 사용법
# sep는 단어와 단어 사이를 어떤 식으로 할지 정하는 것
# end는 마지막에 어떻게 할지 정하는 것
print("red", "green", "blue", sep="*", end="")
print("yellow", "cyan", "magent", sep=",")

# 문자열 곱하기
print("*" * 20)
print("="*40)


# 문자열 포매팅 - 문자, 숫자 섞어서 문장 만들 때 사용한다.
name = "홍길동"
age = 34
height = 182.5
# %자릿수 형식  %10d    f의 경우는 %전체자리수.소수점자리수f
# %를 출력하고 싶을 땐 %%를 사용한다.
s = "%s의 나이는 %04d입니다. 그리고 키는 %.2f입니다. 10%%" % (name, age, height)
print(s)

a = 37
print("8진수 %o" % a)
print("16진수 %x" % a)

print("%10s %10s" % ("hi", "hello"))    # 10자리 확보하고 오른쪽부터 채워온다.
print("%-10s %-10s" % ("hi", "hello"))    # 10자리 확보하고 왼쪽부터 채워온다.

a = 3.141592
print("%f" % a)
print("%.2f" % a)
print("%7.2f" % a)

print("이름: {0}, 나이: {1}".format(name, age))
print("이름: {}, 나이: {}".format(name, age))
print("이름: {_name}, 나이: {_age}".format(_name="홍동", _age=37))
print("이름: {name}, 나이: {age}".format(name=name, age=age))

# 문자열 앞에 f를 쓰고 {변수명} - fstring
# 와! 채신기술!!!
print(f"이름: {name}, 나이: {age}")

print("이름: ", end="")
print(name, end=" ")
print("나이: ", end="")
print(age)

# 정렬
print("{0:<10} {1:<10}".format("hi", "hello"))  # 왼쪽 정렬
print("{0:>10} {1:>10}".format("hi", "hello"))  # 오른쪽 정렬
print("{0:^10} {1:^10}".format("hi", "hello"))  # 가운데 정렬
print("{0:=^10} {0:!^10}".format("hi", "hello"))    # 공백에 어떤 문자를 채울지

print("{0:.4f}".format(3.1415926535897932384626))

x = int(input("x = "))
y = int(input("y = "))
print(f"{x} + {y} = {x+y}")
