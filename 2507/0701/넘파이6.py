import numpy as np

data = np.random.rand(5)
print(data)
np.save("datafile.npy", data)   # 데이터 한 개만 저장 가능

# 불러오기
data2 = np.load('datafile.npy')
print(data2)



