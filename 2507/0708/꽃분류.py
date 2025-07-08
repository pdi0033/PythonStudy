# 1. 파일을 읽어서 numpy 배열로 만들어야 한다.
# 2. 폴더별로 labeling을 해야 한다.

import PIL.Image as pilimg
import os       
import matplotlib.pyplot as plt    
import numpy as np      
import imghdr   # 이미지의 종류를 알아내고자 할 때 사용
import pandas as pd

# makeData => 폴더명하고 라벨을 주면 makeData("daisy", 1)
# 해당 폴더 데이터 쭉 읽어서 numpy배열로 바꾸고 라벨링 작업도 하고
def makeData(folder, label):
    data = []       # 이미지의 피처를 저장 - 마지막에 둘다 반환하기
    labels = []     # 라벨 저장
    path = "../data/flowers" + "/" + folder
    for fileName in os.listdir(path):
        try:
            # print(path + "/" + fileName)
            kind = imghdr.what(path + "/" + fileName)   # 파일의 종류를 확인하기 위한 파이썬 명령어
            # 파일의 확장자를 잘라서 확인해도 되는데? 
            # 확장자는 윈도우 os만 있지, 리눅스는 파일 정보에 종류가 저장
            if kind in ["gif", "png", "jpg", "jpeg"]:   # 이 이미지에 해당되면
                img = pilimg.open(path + "/" + fileName)
                # 이미지 크기가 다르면 분석 불가능, 동일한 이미지 크기로 해야 한다.
                # 그리고 이미지 크기가 너무 크면 학습할 떄 픽처 개수가 너무 많아서 학습이 어렵다.
                # 적당한 크기로 잘라야 한다.
                resize_img = img.resize( (80,80) )      # 크기를 튜플로 전달하면 아ㅠ의 이미지 크기만 변경됨
                pixel = np.array(resize_img)        # 이미지를 -> ndarray로 변경한다.
                if pixel.shape == (80, 80, 3):      # 이미지 크기 같은것만 취급한다.
                    data.append(pixel)
                    labels.append(label)
        except:
            print(fileName + " error ")     # 어떤 파일이 에러인지 찾아서 직접 삭제시키려고

    # 파일로 저장하기
    np.savez("{}.npz".format(folder), data=data, target=labels)

# 1. 파일로 저장하기
def fileSave():
    makeData("daisy", "0")
    makeData("dandelion", "1")
    makeData("sunflower", "2")
    makeData("rose", "3")
    makeData("tulip", "4")
# fileSave()

def loadData():
    daisy = np.load("daisy.npz")
    dandelion = np.load("dandelion.npz")
    sunflower = np.load("sunflower.npz")
    rose = np.load("rose.npz")
    tulip = np.load("tulip.npz")

    data = np.concatenate( (daisy["data"], dandelion["data"], 
                            sunflower["data"], rose["data"], tulip["data"]) )
    target = np.concatenate( (daisy["target"], dandelion["target"], 
                            sunflower["target"], rose["target"], tulip["target"]) )
    print(data.shape)
    print(target.shape)
    return data, target     # 지역변수라서 함수 안에만 존재 리턴을 해주자

data, target = loadData()
# 4차원 머신러닝, 딥러닝 => 딥러닝(CNN, 합성곱신경망). 차원을 그대로 받아들인다.
data = data.reshape(data.shape[0],
                    data.shape[1] * data.shape[2] * data.shape[3])
print(data.shape)
# data = 4317, 80, 80, 3

# 머신러닝의 일부 알고리즘과 딥러닝은 반드시 정규화 또 스케일링 0~1 사이의 값으로 축소시키는 것이 유리함.
data = data/255.0

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0, test_size=0.5)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=0, n_estimators=700, max_depth=3)
model.fit(X_train, y_train)
print("--- 랜덤포레스트 ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

# xgboost
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)
model = XGBClassifier(random_state=0, n_estimators=300, max_depth=3, learning_rate=0.1)
model.fit(X_train, y_train)
print("--- xgboost ---")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

