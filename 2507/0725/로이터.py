from keras.datasets import reuters  # 다중분류
from keras import models, layers
import tensorflow as tf
import keras
import os
from keras.utils import to_categorical

# 머신러닝은 라벨을 원핫인코딩 안함. 딥러닝은 해줘야 한다.
# 케라스 입장에서 문자열 데이터들을 어떤 형태로 numpy배열로 만들었는지를 보고
# imdb 데이터셋 => numpy 배열로 바꿔서 온 거
# 문자열들을 어떤 식으로 numpy배열로 바꿀 것인가? (다음주에)
# 영화평들을 다 읽어서 => numpy배열로 바꾼다. (케라스)
# 빈도수로 파악할 때 자주 쓰는 단어 10000 개만 가져다 쓰겠다.
# num_words=10000 : 빈도수를 기반으로 해서 자주 쓰는 단어 만 개만 가져다 쓰겠다.
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)
# 데이터 개수 확인
print(train_data.shape)
print(train_labels.shape)
print(test_data.shape)
print(test_labels.shape)
# 데이터 자체도 궁금
print(train_data[:3])       # 문장을 list타입으로 가져온다.
print(train_labels[:3])

# 데이터를 시퀀스로 바꿔야 하는데, 시퀀스로 바꾸는 과정은 담주
# get_word_index()
word_index = reuters.get_word_index()
print(type(word_index))
# print(word_index.keys())

def showDictionary(cnt):    # word_index의 내부구조 확인
    i = 0
    for key in word_index.keys():
        if i >= cnt:
            break
        print(key, word_index[key])
        i += 1

showDictionary(10)      # word_index    영어단어: 인덱스
# I like star.  {"I":0, "like":1, "star":2, ....}
# [0, 1, 2]

# 받아온 시퀀스를 문장으로 원복시켜보자.    word_index는 단어:숫자
# reverse_index => 숫자: 단어
reverse_index = [(value, key) for (key, value) in word_index.items()]
for i in range(0, 10):
    print(reverse_index[i])
# dict으로 바꿔야 한 번에 검색함
reverse_index = dict(reverse_index)

# 시퀀스를 문장으로 바꾸기
# 케라스 만든 사람들이 0~3 번까지는 특수목적으로 사용.  인덱스 4부터 쓸모가 있음
def changeSentence(id):
    sequence = train_data[id]
    # 만 개만 가져오니까 없는 단어도 있을 수 있음 그때 두번째 인자로 바꿔준다.
    sentence = ' '.join(reverse_index.get(i-3, "*") for i in sequence )
    print(sentence)

for i in range(5):
    changeSentence(i)

# train_data: 시퀀스 배열 [3, 42, 1, 2, 3]
# 원핫인코딩 - 내부함수 돌 고 한번 만들어보자
import numpy as np
def vectorize_senteces(sequences, dimensions=10000):
    results = np.zeros( (len(sequences), dimensions) )  
    # 문장개수 * 10000 개의 2차원 배열, 0으로 채우는
    # 0, 0, 0, 0, ,,,, ,0
    # 0, 0, 0, 0, ,,,, ,0
    for i, sequence in enumerate(sequences):    # enumerate(list타입) - 인덱스와 요소를 하나씩 전달한다.
        # [1, 4, 11, 12, 6, 5, 4]   해당 위치를 1로 채운다.
        results[i, sequence] = 1.
        # 넘파이배열 a[ [1,2,3,7,8] ]   = 1
    return results

X_train = vectorize_senteces(train_data)    # 시퀀스 => 원핫인코딩
X_test = vectorize_senteces(test_data)    # 시퀀스 => 원핫인코딩
y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)
print(X_train[:3])
print(y_train[:3])
print(len(y_train[0]))

# 훈련셋과 검증셋을 나눈다. - 전체 데이터 8982
# (8982,)
# (2246,)
X_val = X_train[:2000]     # 검증 : 10000 개
X_train = X_train[2000:]   # 훈련 : 15000 개
y_val = y_train[:2000]
y_train = y_train[2000:]

model = models.Sequential()
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=50, batch_size=100, validation_data=(X_val, y_val))

# 평가하기
print("훈련셋", model.evaluate(X_train, y_train))
print("테스트셋", model.evaluate(X_test, y_test))

# 예측하기
pred = model.predict(X_test)
# print(pred[:10])
def predData(pred):
    match_cnt = 0
    for i in range( len(pred) ):
        if np.argmax(y_test[i]) == np.argmax(pred[i]):
            match_cnt += 1
    return match_cnt
match_cnt = predData(pred)
print(f"총 데이터 개수:{len(pred)}, 맞춘 개수: {match_cnt}, 틀린 개수: {len(pred)-match_cnt}")


# 훈련과 검증 정확도 그리기
import matplotlib.pyplot as plt
history_dict = history.history
acc = history_dict['accuracy']      # 훈련셋 정확도
val_acc = history_dict['val_accuracy']  # 검증셋 정확도

length = range(1, len(history_dict['accuracy'])+1 )     # x축 만들기
plt.plot(length, acc, 'bo', label='Training acc')
plt.plot(length, val_acc, 'b', label='Validation acc')
plt.title("Training and Validation acc")
plt.xlabel('Epochs')
plt.ylabel('Acc')
plt.legend()
plt.show()

