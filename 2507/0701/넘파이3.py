import numpy as np

# range함수 대신=> arange(시작값, 엔딩값, 증감치)
# for 나 lsit 필요없음
print(np.arange(1,11))
print(np.arange(1,11, 0.1))
print(np.arange(1,11, 2))
print(np.arange(0,1, 0.2))
print(np.arange(10, 0, -1))

# 복사하기 - 얕은 복사
a = np.arange(1,11)
b = a   # 얕은 복사
a[0] = 100
print(a)
print(b)

c = a.copy()    # 깊은 복사
c[0] = -1
print(a)
print(c)

# 메모리 할당을 해서 요소의 값이 0이나 1로 채워진 ndarray 타입 만들기
a = np.zeros(10)
print(a)

b = np.zeros((2,10))
print(b)

b = np.zeros((3,4,5))   # 매개변수가 tuple 타입임
print(b)

c = np.ones((3,10))
print(c)

# 요소가 랜덤인 배열 또는 행렬 생성
# 평균이 0분산 1인 가우스분포(정규 분포)를 따르는 난수 발생.
print(np.random.rand(10))
print(np.random.rand(2,3))
print(np.random.rand(2,3,4))

# 정수발생 np.random.randint(low, high, size) low~high값을 size만큼 만든다.
print(np.random.randint(10,20,4))
print(np.random.randint(10,20, (2,3)))

# 차원변환
a = np.arange(10)
a = a.reshape(2,5)
print(a)
a = a.reshape(5,2)
print(a)

# a = np.array
a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,10])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

