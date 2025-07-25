from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import PIL.Image as pilimg
import os      
import imghdr
import numpy as np
import pandas as pd
from keras.utils import to_categorical

# 데이터만들기 folder를 읽어서 데이터를 만들어보자 - train 폴더
base_path = "../data/flowers2"
def makeData(flower_name, label, isTrain=True):     # train/daisy 0   train/dandelion 1
    if isTrain:
        path = base_path + '/train/' + flower_name
    else:
        path = base_path + '/test/' + flower_name
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

    title = "train"
    if not isTrain:
        title = "test"
    savefileName = "imagedata{}.npz".format(str(label) + "_" + title)
    np.savez(savefileName, data=data, target=labels)

def initData():
    flowers = ["daisy", "dandelion"]
    i = 0
    for f in flowers:
        makeData(f, i, True)
        makeData(f, i, False)
        i += 1

def loadData():
    f1 = np.load("imagedata0_train.npz")
    f2 = np.load("imagedata1_train.npz")

    d1 = f1["data"]
    t1 = f1["target"]

    d2 = f2["data"]
    t2 = f2["target"]

    X_train = np.concatenate( (d1, d2), axis=0 )
    y_train = np.concatenate( (t1, t2), axis=0 )

    f1 = np.load("imagedata0_test.npz")
    f2 = np.load("imagedata1_test.npz")

    d1 = f1["data"]
    t1 = f1["target"]

    d2 = f2["data"]
    t2 = f2["target"]

    X_test = np.concatenate( (d1, d2), axis=0 )
    y_test = np.concatenate( (t1, t2), axis=0 )

    return X_train, y_train, X_test, y_test

from tensorflow.keras import models, layers
def createModel():
    network = models.Sequential(
        [
            layers.Rescaling( 1. / 255.0 ),     # 스케일링
            layers.Conv2D(64, (3,3), activation='relu'),    # 층은 마음대로 한 것
            layers.MaxPooling2D((2,2)),                     # 결과가 과대적합이 되었으면 조절해야함.
            layers.Conv2D(32, (3,3), activation='relu'),
            layers.Conv2D(32, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(32, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Flatten(),

            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(32, activation='relu'),
            layers.Dense(2, activation='softmax')   
            # 2진 분류일 때는 결과값 1개이고, 활성화함수는 sigmoid
            # 암인지 아닌지. target이 악성:0, 양성:1
            # 1(양성)이 될 확률을 출력 => 예측확률 => 양성일 확률이 출력된다.
            # 악성이 될 확률은 (1 - 양성확률)
            # target을 0->1으로 바꾸고 1->0으로 바꾸기
            # 2, softmax
        ]
    )

    # loss 이진분류일 때는 binary_crossentropy
    network.compile(optimizer='rmsprop',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])
    return network

from sklearn.preprocessing import StandardScaler
def preprocessing():
    X_train, y_train, X_test, y_test = loadData()
    # 차원이 현재 4차원 => 2차원으로
    # X_train = X_train.reshape(X_train.shape[0], 80*80*3)
    # X_test = X_test.reshape(X_test.shape[0], 80*80*3)
    # scaler = StandardScaler()
    # X_train_scaled = X_train / 255.0
    # X_test_scaled = X_test / 255.0

    return X_train, y_train, X_test, y_test

def main():
    X_train, y_train, X_test, y_test = preprocessing()
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    network = createModel()
    network.fit(X_train, y_train, epochs=10, batch_size=100)

    train_loss, train_acc = network.evaluate(X_train, y_train)
    test_loss, test_acc = network.evaluate(X_test, y_test)
    print(f"훈련셋 손실값: {train_loss}, 정확도: {train_acc}")
    print(f"테스트셋 손실값: {test_loss}, 정확도: {test_acc}")

if __name__ == "__main__":
    main()
    # initData()
    # X_train, y_train, X_test, y_test = preprocessing()


# 한시간 => 젤 높은 점수한테 커피쿠폰, 훈련셋하고 테스트셋 차이도 작고

# 훈련셋 손실값: 0.21295663714408875, 정확도: 0.9137254953384399
# 테스트셋 손실값: 0.4316278100013733, 정확도: 0.8131868243217468

# 훈련셋 손실값: 0.3851039409637451, 정확도: 0.843137264251709
# 테스트셋 손실값: 0.42821410298347473, 정확도: 0.807692289352417
