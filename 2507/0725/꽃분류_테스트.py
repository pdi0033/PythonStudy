# 폴더에 train, test, validation 등으로 나눈 다음에 
# 각자 폴더에 라벨을 만들고 데이터 넣어놓고, 
# ImageDataGenerator나 DataSet을 통해서 파일을 직접 읽어서 학습한다.

# 데이터 증강. ImageDataGenerator(초창기부터) - 폴더로부터 직접 이미지 파일을 읽어서 각종 처리를 해서 원하는만큼 데이터를 늘려서 가져온다.
# 좀더 정밀하게 비슷한 일을 한다. DataSet - Tensor 2.xx이후 추가
# 이미지 => numpy배열로 바꿔서 학습: 데이터가 충분히 많으면

# 데이터셋이 작을 때 이미 학습된 CNN하고 작업할 때 쓸 예정임
# 1. cats_and_dogs_small - train, test, validation
#   train/cat - 고양이사진 1000장, dog - 개사진 1000장
#   test/cat - 고양이사진 500장, dog - 개사진 500장
#   validation/cat - 고양이사진 500장, dog - 개사진 500장

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 
import pickle 
import keras 
import os
import shutil       # 디렉토리 만들기, 삭제 등을 담당하는 라이브러리

# 학습모델(네트워크) - 학습을 완료한 모델을 저장시켜놓고 불러다가 예측을 할 수 있다.
model_save_path_keras = "./flowers2/flowers2.keras"     # 확장자가 h5 => keras로 바뀜
# 케라스가 지원한다.
history_filepath = './flowers2/flowers2.bin'
# 학습을 할 때마다 정확도, 손실값이 있고 저장해서 던져준다.
# 이 값 자체는 저장을 지원하지 않는다. 그래서 pickle을 써서 저장하는데
# 희한하게도 history 자체로 저장하면 에러나고 history.history를 저장해야 에러가 안 난다.

def ImageCopy():
    pass

from keras import models, layers
# DataSet 사용하기
def deeplearning():
    pass

def drawChart():
    print("저장된 모듈 불러오기")
    try:
        loaded_model_keras = keras.models.load_model(model_save_path_keras)
        print("모델 부르기 성공")
    except Exception as e:
        print(f"모델 로딩중 실패 : {e}")
    
    print("히스토리 불러오기")
    try:
        with open(history_filepath, 'rb') as file:
            history = pickle.load(file)
            print("히스토리 로딩 성공")
    except Exception as e:
        print(f"히스토리 로딩중 실패 : {e}")
    
    # 히스토리의 키값들 가져오기 - 에포크 회수만큼 list로 가져온다.
    acc = history['accuracy']
    val_acc = history['val_accuracy']
    loss = history['loss']
    val_loss = history['val_loss']

    # X축 좌표값 만들기
    X = range(len(acc))

    plt.plot(X, acc, 'ro', label='Training accuracy')
    plt.plot(X, val_acc, 'b', label='Validation accuracy')
    plt.title("Training and Validation accuracy")

    # 새로운 창을 열어 차트를 그린다.
    plt.figure()    # 새로운 창을 만든다.
    plt.plot(X, loss, 'ro', label='Training loss')
    plt.plot(X, val_loss, 'b', label='Validation loss')
    plt.title("Training and Validation loss")

    plt.show()      # 전체 한번에 출력

def Predict():  # 예측하기
    # 1. 학습된 모듈을 불러온다.
    loaded_model_keras = None
    try:
        loaded_model_keras = keras.models.load_model(model_save_path_keras)
        print("모델 부르기 성공")
    except Exception as e:
        print(f"모델 로딩중 실패 : {e}")
        return

    # 예측데이터셋
    val_ds = keras.utils.image_dataset_from_directory(
        os.path.join("../../data/flowers_small", "test"),  # 폴더를 지정한다.
        validation_split=0.2,   # 훈련셋을 훈련셋과 검증셋으로 8:2구조로 나눠서 검증
        seed=123,
        subset="validation",
        image_size=(180, 180),
        batch_size=16
    )

    print("----- 라벨링 -----")
    class_names = val_ds.class_names
    print(class_names)

    total_match_count = 0       # 전체 일치한 개수
    total_samples_proceed = 0   # 전체 처리 개수
    max_samples_to_process = 163    # 데이터를 500개까지만 예측해보자
    for input_batch, labels_batch in val_ds:
        # val_ds가 폴더로부터 이미지 파일을 읽어오는데 batch_size만큼씩 읽어온다.
        total_samples_proceed += len(labels_batch)
        
        # 예측하기
        predictions_batch = loaded_model_keras.predict(input_batch, verbose=2)
        predicted_class = np.argmax(predictions_batch, axis=1)
        
        matches = (labels_batch.numpy() == predicted_class)
        total_match_count += np.sum(matches)

        # if total_samples_proceed >= max_samples_to_process:
        #     print(f"처리된 샘플 수가 {max_samples_to_process}개를 초과하여 중단합니다.")
        #     break
    
    # print(total_samples_proceed, len(labels_batch))
    print("전체 데이터 개수:", total_samples_proceed)
    print("맞춘 개수:", total_match_count)
    print("틀린 개수:", total_samples_proceed - total_match_count)
    print("정확도:", total_match_count / total_samples_proceed)


def main():
    while True:
        print("1. 파일복사")
        print("2. 학습")
        print("3. 차트")
        print("4. 예측")
        sel = input("선택 >> ")
        if sel == "1":
            ImageCopy()
        elif sel == "2":
            deeplearning()
        elif sel == "3":
            drawChart()
        elif sel == "4":
            Predict()
        else:
            break


if __name__ == "__main__":
    main()






