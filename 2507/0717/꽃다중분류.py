from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import PIL.Image as pilimg
import os      
import imghdr
import numpy as np
import pandas as pd

tf.random.set_seed(1)

# 데이터 불러오기
def makeData(folder, label):
    data = []
    labels = []
    path = "../data/flowers" + "/" + folder
    for fileName in os.listdir(path):
        try:
            kind = imghdr.what(path + "/" + fileName)
            if kind in ["gif", "png", "jpg", "jpeg"]:
                img = pilimg.open(path + "/" + fileName)
                resize_img = img.resize( (80,80) )      # 크기를 튜플로 전달하면 아ㅠ의 이미지 크기만 변경됨
                pixel = np.array(resize_img)        # 이미지를 -> ndarray로 변경한다.
                if pixel.shape == (80, 80, 3):      # 이미지 크기 같은것만 취급한다.
                    data.append(pixel)
                    labels.append(label)
        except:
            print(fileName + " error ")
    # 파일로 저장하기
    np.savez("{}.npz".format(folder), data=data, target=labels)

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
    return data, target 

data, target = loadData()

# 데이터 처리 -> 차원변환, 스케일링
data = data.reshape(data.shape[0],
                    data.shape[1] * data.shape[2] * data.shape[3])
print(data.shape)

data = data.astype(float)/255.0

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=1, test_size=0.2)

# 딥러닝은 라벨도 원핫인코딩 해야 한다.
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 네트워크 구축하기
network = keras.models.Sequential([
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64, activation='relu'),   # 히든충 추가 - 내마음
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dense(5, activation='softmax')
])

# 컴파일 옵티마이저, 손실함수, 평가척도 지정
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 학습하기
history = network.fit(X_train, y_train, epochs=30, batch_size=100)

# 평가하기
train_loss, train_acc = network.evaluate(X_train, y_train)
print(f"훈련셋 손실: {train_loss}, 정확도: {train_acc}")
test_loss, test_acc = network.evaluate(X_test, y_test)
print(f"테스트셋 손실: {test_loss}, 정확도: {test_acc}")
