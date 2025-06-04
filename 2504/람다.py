def add(x=0, y=0, z=0):     # 함수는 그 자체가 주소이다.
    return x+y+z

myadd = add     # myadd라는 변수에 add함수 주소가 들어간다.
print( myadd(3,4,5) )

# 함수의 매개변수로 함수를 줄 수 있다.
def myfunc(x,y, callback):  # 세 번째 인자가 callback - 함수 주소를 받아옴
    result = callback(x, y)
    print(x, y, result)

def add(x, y):
    return x+y

myfunc(4,5, add)    # 함수 주소를 전달한다.
# 임시 함수를 만든다. lambda로 시작해야 하고 이름은 없으며 두 개의 매개 변수를 가져야 한다.
# :(콜론) 뒤에는 함수의 내용을 기술하면 되고 return은 생략이다.
myfunc(4,5, lambda x, y: x-y)

fucList = [
    lambda x, y: x+y,
    lambda x, y: x-y,
    lambda x, y: x*y,
    lambda x, y: x/y
]

for fun in fucList:
    print( fun(9,7) )


# 앞에 함수, 두 번째 인자에 iterable이 온다.
# 특정 조건에 맞는 데이터의 iterable 타입을 반환한다.

a = [1,2,3,4,5,6,7,8,10]
# 첫 번째 매개변수로 올 함수를 호출하는 호출자는 filter임
# 매개변수가 하나이어야 하고, 반환값을 bool타입(True 또는 False) 이어야 함
def isEven(n):
    return n%2 == 0

for i in filter(isEven, a):
    print(i)
    
for i in filter(lambda x: x%2 == 0, a):
    print(i)

personList = [
    {"name": "홍길동", "age": 34, "phone": "010-0000-0001"},
    {"name": "강감찬", "age": 70, "phone": "010-0000-0002"},
    {"name": "서희",   "age": 54, "phone": "010-0000-0003"},
    {"name": "윤관",   "age": 39, "phone": "010-0000-0004"},
    {"name": "김종서", "age": 38, "phone": "010-0000-0005"},
    {"name": "이순신", "age": 44, "phone": "010-0000-0006"},
    {"name": "곽재우", "age": 62, "phone": "010-0000-0007"}
]

# 이름이 서희인 사람의 자료를 갖고 오고자 한다.
# filter personList를 가져 갔으니까 람다의 매개변수도 personList 안의 dict 객체
# 반환 값도 dict 객체
keyName = "서희"
for person in filter(lambda e: e["name"] == keyName, personList):
    print(f"{person["name"]} {person["age"]} {person["phone"]}")

# filter를 감싸고 있는 list가 filter를 동작을 시키고 결과들을 list로 만들어서 반환한다.
findList = ( list( filter(lambda e: e["name"] == keyName, personList) ) )
print(findList)
print()

# 40세 이상만
findList = ( list( filter(lambda e: e["age"] >= 40, personList) ) )
for i in findList:
    print(i)

# map, sort: 정렬, zip: 다른 언어에 없음
# map - 연산을 수행한다.    나이 - 5
# 첫 번째 매개변수가 매개변수 하나 값 하나를 반환하는 함수이어야 한다.
for i in map(lambda x: x*10, a):
    print(i)
print()

def myFunc2(x):
    x["age"] += 5
    return x

for per in map(myFunc2, personList):
    print(per)

# 데이터 정렬
# list 타입 자체가 sort 메서드가 있다.
a = [9,4,5,6,7,8,1,2,10,3]
a.sort()    # 내부 데이터가 정렬된다.
print(a)

personList.sort(key= lambda x: x["name"])   # 정렬을 할 때 a[0] < a[1]
print(personList)

personList.sort(key= lambda x: x["name"], reverse=True)   # 정렬을 할 때 a[0] < a[1]
print(personList)

a = [9,4,5,6,7,8,1,2,10,3]
b = sorted(a)
print("a=", a)
print("b=", b)

personList = [
    {"name": "홍길동", "age": 34, "phone": "010-0000-0001"},
    {"name": "강감찬", "age": 70, "phone": "010-0000-0002"},
    {"name": "서희",   "age": 54, "phone": "010-0000-0003"},
    {"name": "윤관",   "age": 39, "phone": "010-0000-0004"},
    {"name": "김종서", "age": 38, "phone": "010-0000-0005"},
    {"name": "이순신", "age": 44, "phone": "010-0000-0006"},
    {"name": "곽재우", "age": 62, "phone": "010-0000-0007"}
]

sorted_personList = sorted(personList, key= lambda per: per["name"])
for i in personList:
    print(i)
print()

for i in sorted_personList:
    print(i)


# zip 함수
a = ["a", "b", "c", "d", "e"]
b = [1,2,3,4,5]
for item in zip(a,b,a):
    print(item)