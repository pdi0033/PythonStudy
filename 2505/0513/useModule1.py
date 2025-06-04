#외부 모듈을 사용하기
import mod1     #파일 전체가 메모리에 로딩된다.
print(mod1.add(3,4))
print(mod1.sub(3,4))

p2 = mod1.Person("윤하", 44)
p2.print()

import mod1 as md   #모듈명이 길 경우 aliasing 다른 이름으로 부를 수 있다
print(md.add(3,4))
print(md.sub(3,4))

p2 = md.Person("웬디", 32)
p2.print()

# 파일명 쓰기 싫고 마치 내함수처럼 쓰고 싶다.
from mod1 import add, sub
print(add(9,8))
print(sub(9,8))

from mod1 import Person
p3 = Person("조이", 24)
p3.print()

# numpy는 수학 라이브러리다.
# 수학 라이브러리 -> 머신러닝의 경우 무조건 numpy타입으로 전환해야 한다.
import numpy as np
a = [1,2,3,4,5,6,7,8,9,10]
b = [x*2 for x in a]
c = a + b
print(a)
print(b)
print(c)

a1 = np.array(a)
b1 = 2 * a1
c1 = a1 + b1
print(a1)
print(b1)
print(c1)