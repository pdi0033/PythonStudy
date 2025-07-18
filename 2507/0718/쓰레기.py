from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import PIL.Image as pilimg
import os      
import imghdr
import numpy as np
import pandas as pd

# 데이터만들기 folder를 읽어서 데이터를 만들어보자 - train 폴더
base_path = "../data/garbage/Garbage classification/Garbage classification"
def makeData(garbage_name, label):     # train/daisy 0   train/dandelion 1
    path = base_path + '/' + garbage_name
    # print(path)
    data = []
    labels = []
    # print(os.listdir(path))     # 해당 경로에 파일명을 모두 가져온다.
    # 파일 하나씩 읽어서 넘파이배열로 만들어서 data에 추가시키기
    i = 1
    for filename in os.listdir(path):
        try:
            if i%100 == 0:
                print(f"{i} 번째 파일 처리중 ....")
            i+=1

            # 파일 속성도 확인해보자
            kind = imghdr.what(path + "/" + filename)
            if kind in ['gif', 'png', 'jpeg', 'jpg']:   # 이미지일 때만
                img = pilimg.open(path + "/" + filename)    # 파일을 읽어서 numpy 배열로 바꾼다.
                resize_img = img.resize( (80, 80) )  # 사이즈는 특성이 너무 많으면 계산시간도 오래 걸리고
                                                    # 크기가 각각이면 학습 불가능. 그래서 적당한 크기를 맞춘다.
                pixel = np.array(resize_img)
                if pixel.shape == (80, 80, 3):
                    data.append(pixel)
                    labels.append(label)
        except:
            print(filename + " error")

    savefileName = "garbage/imagedata{}.npz".format(str(label) + "_" + garbage_name)
    np.savez(savefileName, data=data, target=labels)

def initData():
    garbages = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
    i = 0
    for f in garbages:
        makeData(f, i)
        i += 1

def loadData():
    X = None
    y = None

    for filename in os.listdir("./garbage"):
        f1 = np.load("./garbage/" + filename)

        d1 = f1["data"]
        t1 = f1["target"]

        if X is None:
            X = d1
            y = t1
        else:
            X = np.concatenate((X, d1), axis=0)
            y = np.concatenate((y, t1), axis=0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    return X_train, y_train, X_test, y_test

from tensorflow.keras import models, layers
def createModel():
    network = models.Sequential(
        [
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(32, activation='relu'),
            layers.Dense(6, activation='softmax')
        ]
    )

    network.compile(optimizer='rmsprop',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])
    return network

from sklearn.preprocessing import StandardScaler
def preprocessing():
    X_train, y_train, X_test, y_test = loadData()
    # 차원이 현재 4차원 => 2차원으로
    X_train = X_train.reshape(X_train.shape[0], 
                              X_train.shape[1] * X_train.shape[2]* X_train.shape[3])
    X_test = X_test.reshape(X_test.shape[0],
                            X_test.shape[1] * X_test.shape[2]* X_test.shape[3])
    scaler = StandardScaler()
    # X_train_scaled = scaler.fit_transform(X_train)
    # X_test_scaled = scaler.fit_transform(X_test)

    X_train_scaled = X_train.astype(float)/255.0
    X_test_scaled = X_test.astype(float)/255.0

    return X_train_scaled, y_train, X_test_scaled, y_test

def main():
    X_train, y_train, X_test, y_test = preprocessing()
    network = createModel()
    network.fit(X_train, y_train, epochs=70, batch_size=100)

    train_loss, train_acc = network.evaluate(X_train, y_train)
    test_loss, test_acc = network.evaluate(X_test, y_test)
    print(f"훈련셋 손실값: {train_loss}, 정확도: {train_acc}")
    print(f"테스트셋 손실값: {test_loss}, 정확도: {test_acc}")

if __name__ == "__main__":
    main()
    # initData()
    # X_train, y_train, X_test, y_test = preprocessing()
    # print(X_train.shape)
    # # print(X_train[:5])
    # print(y_train.shape)
    # # print(y_train[:5])
    # print(X_test.shape)
    # # print(X_test[:5])
    # print(y_test.shape)
    # # print(y_test[:5])


