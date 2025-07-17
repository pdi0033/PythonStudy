from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

tf.random.set_seed(1)

# 1.데이터 가져오기
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234)

print(X_train.shape, y_train.shape)   # (60000, 28, 28) (60000,)
print(X_test.shape, y_test.shape)     # (10000, 28, 28) (10000,)

# 2. 딥러닝 모델을 만든다.
from tensorflow.keras import models, layers

# 네트워크 또는 모델이라고 부른다.
# keras.Sequenctial 로 모델을 만드는데 매개변수로 list타입 안에 레이어 객체를 전달한다.
model = keras.Sequential([
    # 2-1. 입력층을 설계한다.
    # layers.Dense(출력값의개수, 활성화함수, 입력데이터의 크기-생략가능)
    # 출력값의 개수? 저 계층을 나왔을 때 가져올 가중치들의 개수. 내 마음대로 설정.
    # 출력값의 개수를 너무 크게 주면 메모리 부족도 있고, 과대적합 문제도 있음. 적당히. 2의 배수로 많이들 준다.
    layers.Dense(256, activation='relu'),
    # 2-2. 중간에 다른층 추가 가능
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),

    # 2-3. 출력층. 마지막 층은 라벨에 맞춘다. 즉 결과를 얻기 위한 층이다.
    #       손으로 쓴 숫자니까 0,1,2,...,9까지 10개 중 하나이어야 한다. 
    #       딥러닝의 분류는 출력데이터를 확률로 반환한다. 예) [0.1, 0.1, 0.05, 0.7, ...] 결과는 3으로 판단한다.
    #       각 층을 거치면서 나오는 값들은 실제는 확률이 아니고 엄청 큰 값들이다.
    #       이걸 모두 합해서 1이 되는 확률로 전환해야하는데 이 함수가 softmax함수이다.
    #       다중분류의 출력층의 활성화 함수는 무조건 softmax함수이다.
    layers.Dense(3, activation='softmax')  # 출력값의 개수, 활성화함수
    # 회귀랑 이진분류랑 다중분류랑 다 다르게 작성해야 한다.
    # 회귀의 경우 출력층:    layers.Dense(1)
    # 이진분류의 경우 출력층: layers.Dense(1, activation='sigmoid')
])
# 네트워크 또는 모델을 만들다라고 표현한다.
# compile에서 손실함수, 옵티마이저, 평가지표를 지정한다.
# sparse_categorical_crossentropy 희한하게 딥러닝은 라벨도 원핫인코딩
# 머신러닝은 라벨을 원핫인코딩, 원핫인코딩 자동으로 해준다.
model.compile(optimizer='rmsprop', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

# 3. 데이터관련 작업
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)     # 스케일링

# loss='sparse_categorical_crossentropy'(정수인코딩), 이거 안 쓰고 categorical_crossentropy 쓰면 원핫인코딩
# 라벨도 원핫인코딩을 해야 한다. 머신러닝하고 차이점

# 학습하기 => 학습하는 과정 속에 있었던 내용을 (history)를 반환한다.
hist = model.fit(
    X_train,   # X, 독립변수, 입력값
    y_train,   # y, 종속변수, 목표, 출력값
    epochs = 100,     # 학습회수
    batch_size = 128    # 데이터를 메모리를 불러올 때의 크기지정. 너무 크면 메모리 부족.
                        # 너무 작으면 속도가 느리다. 전체 데이터를 batch_size만큼 불러서 학습하고 끝나면 1에포크라고 한다.
)

# 평가 evaluate 함수를 사용한다.
train_loss, train_acc = model.evaluate(X_train, y_train)
print(f"훈련셋 손실: {train_loss}, 정확도: {train_acc}")
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"테스트셋 손실: {test_loss}, 정확도: {test_acc}")



