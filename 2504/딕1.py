# 키 값은 보통 문자열을 주로 사용한다.
# 만일 같은 키 값을 두 번 쓰면 두 번째 것으로 업데이트 한다.

colors = { "red": "빨간색", "blue": "파란색", "green": "초록색"}

# 인데깅, 슬라이싱 불가능
print(colors["red"])
print(colors["blue"])
print(colors["green"])

# 키 값들의 목록을 보여준다.
print(colors.keys(), type(colors.keys()))

# 기존에 없던 키 값을 넣으면 추가된다.
colors["black"] = "검은색"
print(colors)
# 기존에 있는 키 값을 설정하면 설정한 value 값으로 업데이트 된다.
colors["red"] = "빨강"
print(colors)

# 없는 키 값의 경우 파이썬이 어떻게 동작하는지
# print(colors["pink"])   # KeyError: 'pink'
if "pink" in colors.keys():
    print(colors["pink"])
else:
    print("pink is not exist")

# [(키, 값), (키, 값)]
print(colors.items(), type(colors.items()))
# value만
print(colors.values(), type(colors.values()))

# 요소 전부 삭제
colors.clear()
print(colors)

# 특정 키 삭제 - .pop(키)
colors = { "red": "빨간색", "blue": "파란색", "green": "초록색"}
print(colors.pop("red"))
print(colors)

