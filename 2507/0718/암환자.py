from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

def loadData():
    cancer = load_breast_cancer()
    X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    y = cancer.target

    y_changed = np.where(y==0, 1, 0)

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
            layers.Dense(1, activation='sigmoid')   
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
                    loss='binary_crossentropy',
                    metrics=['accuracy'])
    return network

from sklearn.preprocessing import StandardScaler
def preprocessing():
    X_train, y_train, X_test, y_test = loadData()
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    return X_train_scaled, y_train, X_test_scaled, y_test

def main():
    X_train, y_train, X_test, y_test = preprocessing()
    network = createModel()
    network.fit(X_train, y_train, epochs=50, batch_size=100)

    train_loss, train_acc = network.evaluate(X_train, y_train)
    test_loss, test_acc = network.evaluate(X_test, y_test)
    print(f"훈련셋 손실값: {train_loss}, 정확도: {train_acc}")
    print(f"테스트셋 손실값: {test_loss}, 정확도: {test_acc}")

if __name__ == "__main__":
    main()
