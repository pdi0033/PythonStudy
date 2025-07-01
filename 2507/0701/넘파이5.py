import numpy as np

a = np.random.rand(20)
print(a)
print(np.max(a), np.argmax(a))      # argmax는 큰 값이 있는 위치값을 반환한다.

np.random.seed(1234)    # 0~아무값. 이후의 값에 영향을 준다.
a = np.random.random(5)
print(a)
print(np.max(a), np.argmax(a))

a = np.random.random(5)
print(a)
print(np.max(a), np.argmax(a))

# 문제1. 가우스 분포에 따른 랜덤값을 5개씩 10개 생성해서 각 행마다 젤 큰값하고 큰값 위치 찾아서 출력하기
print("="*20)
a = np.random.rand(5,10)
for b in a:
    print(np.max(b), np.argmax(b))
print("="*20)
a = np.random.rand(50)
a = a.reshape(10,5)
for i in range(0,10):
    print(np.argmax(a[i]), np.max(a[i]))



