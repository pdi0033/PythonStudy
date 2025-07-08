import PIL.Image as pilimg
import os       # 파이썬에서 os 명령어를 사용할 수 있게 해준다.
                # 디렉토리 검색해서 해당디렉토리의 파일 목록을 통째로
import matplotlib.pyplot as plt    # 모든 그래픽 출력은 모두 pyplot으로 해야 한다.
import numpy as np      # 이미지 읽어서 numpy 배열로 바꾸기

# 특정폴더의 이미지를 읽어서 전부 numpy 배열로 바꾸고 다 더해서 npz 파일로 저장하기
# 이미지(4차원, 3차원 이미지가 여러 장이라서)를 2차원 ndarray로 바꾸는 방법

# 해보기
path = "../data/images/mnist"
fileNameList = os.listdir(path)
imageList = []
i = 0
for fileName in fileNameList:
    filePath = path + "/" + fileName
    temp = pilimg.open(filePath)
    img = temp.resize( (80,80) )
    img = np.array(img)
    imageList.append(img)
    i += 1
    if i >= 10:
        break
    
# np.savez("data2.npz", data=imageList)

# data2 = np.load("data2.npz")["data"]
# plt.figure(figsize=(20,5))
# for i in range(1, len(data2)+1):
#     plt.subplot(1, 10, i)
#     plt.imshow(data2[i-1])
# plt.show()

# 압축을 푸시면 daisy, dandalion, rose, sunflower, tulip
# 이 이미지들로 머신러닝을 하고 싶다. 입력데이터는 무조건 2d, 라벨링은 1d 폴더별로 0,1,2,3,4
path = "../data/flowers"
fileNameList = os.listdir(path)
targetList = []
imageList = []
i = 0
for folderName in fileNameList:
    folderPath = path + "/" + folderName
    folderNameList = os.listdir(folderPath)
    for fileName in folderNameList:
        filePath = folderPath + "/" + fileName
        temp = pilimg.open(filePath)
        img = temp.resize( (80,80) )
        img = np.array(img)
        imageList.append(img)
        targetList.append(i)
    i += 1

imageList_np = np.array(imageList)
targetList_np = np.array(targetList)

np.savez("data3.npz", data=imageList_np, labels=targetList_np)
data3 = np.load("data3.npz")["data"]
labels = np.load("data3.npz")["labels"]
plt.figure(figsize=(20,5))
for i in range(1, 10):
    plt.subplot(1, 10, i)
    plt.imshow(data3[i-1])
# plt.show()

print(data3.shape, labels.shape)
num_samples = data3.shape[0]
num_features = data3.shape[1] * data3.shape[2] * data3.shape[3]

X = data3.reshape(num_samples, num_features)
print(X[:10])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, labels, random_state=1, test_size=0.3)

# Knn이웃
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("--- Knn이웃 ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

# 로지스틱
# from sklearn.linear_model import LogisticRegression     # 분류
# model = LogisticRegression(solver='liblinear',
#                            multi_class='auto',
#                            max_iter=5000,
#                            random_state=0)
# # solver: 모델계수를 찾아가는 방법. 보통 데이터셋이 적을 때는 liblinear를 써라.
# # multi_class='auto'  : 다중분류일 때
# # max_iter=5000   : 계수 찾아갈 때 학습을 얼마나 반복할까를 지정하는 것
# model.fit(X_train, y_train)
# print("--- 로지스틱회귀 ---")
# print("훈련셋:", model.score(X_train, y_train))
# print("테스트셋:", model.score(X_test, y_test))

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=0, n_estimators=700, max_depth=3)
model.fit(X_train, y_train)
print("--- 랜덤포레스트 ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

# 그라디언트부스팅
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(random_state=0, n_estimators=300, max_depth=3, learning_rate=0.1)
model.fit(X_train, y_train)
print("--- 그라디언트부스팅 ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

# xgboost
from xgboost import XGBClassifier
model = XGBClassifier(random_state=0, n_estimators=300, max_depth=3, learning_rate=0.1)
model.fit(X_train, y_train)
print("--- xgboost ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))