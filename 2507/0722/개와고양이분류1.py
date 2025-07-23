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

# 원본데이터셋이 있는 위치 경로
original_dataset_dir = "../../data/cats_and_dogs/train"

# 옮길 위치 - 기본 폴더
base_dir = "../../data/cats_and_dogs_small"

train_dir = os.path.join(base_dir, "train")
test_dir = os.path.join(base_dir, "test")
validation_dir = os.path.join(base_dir, "validation")

# ImageDataGenerator나 DataSet이나 둘 다 폴더보고 자동으로 라벨링을 한다.
train_cats_dir = os.path.join(train_dir, "cats")
train_dogs_dir = os.path.join(train_dir, "dogs")
test_cats_dir = os.path.join(test_dir, "cats")
test_dogs_dir = os.path.join(test_dir, "dogs")
validation_cats_dir = os.path.join(validation_dir, "cats")
validation_dogs_dir = os.path.join(validation_dir, "dogs")

def ImageCopy():
    # 디렉토리 내의 파일 개수 알아내기
    totalCount = len(os.listdir(original_dataset_dir))
    print("전체 개수: ", totalCount)

    # 반복적인 실행을 위해서 디렉토리 삭제
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir, ignore_errors=True, onerror=None)

    # 디렉토리 만들고
    os.makedirs(base_dir)

    os.makedirs(train_dir)
    os.makedirs(test_dir)
    os.makedirs(validation_dir)

    os.makedirs(train_cats_dir)
    os.makedirs(train_dogs_dir)
    os.makedirs(test_cats_dir)
    os.makedirs(test_dogs_dir)
    os.makedirs(validation_cats_dir)
    os.makedirs(validation_dogs_dir)

    # 파일 옮기기
    # 옮길 파일명이 cat.0.jpg, cat.1.jpg, ,,, cat.1000.jpg
    fnames = [ f'cat.{i}.jpg' for i in range(1000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_cats_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

    fnames = [ f'cat.{i}.jpg' for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_cats_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

    fnames = [ f'cat.{i}.jpg' for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_cats_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

    fnames = [ f'dog.{i}.jpg' for i in range(1000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_dogs_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

    fnames = [ f'dog.{i}.jpg' for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(test_dogs_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

    fnames = [ f'dog.{i}.jpg' for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(validation_dogs_dir, fname)
        shutil.copyfile(src, dst)   # 1개씩 복사

# ImageCopy()   # 복사 끝남

from keras import models, layers
# DataSet 사용하기
def deeplearning():
    # 데이터 증강 파라미터 -> 에포크마다 데이터를 조금씩 변형해서 가져온다.
    # 과대적합을 막기 위해서.
    data_augmentation = keras.Sequential([
        layers.RandomFlip("horizontal", input_shape=(180, 180, 3)), # 이미지를 수평으로 무작위로 뒤집습니다.
        layers.RandomRotation(0.1),     # 이미지를 최대 2pi 라디안의 10(즉, 36도)까지 무작위로 회전시킵니다.
        layers.RandomZoom(0.1),         # 이미지를 최대 10%까지 무작위로 확대하거나 축소합니다.
    ])

    model = models.Sequential()
    # 이미지 스케일링
    model.add(layers.Rescaling(1./255))
    model.add(data_augmentation)    ###
    model.add(layers.Conv2D(32, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(32, (3,3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))      # 중간에 데이터를 절반쯤 없애서 과대적합을 방지
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    # 데이터셋 - 폴더로부터 이미지 파일을 읽어온다.
    train_ds = keras.utils.image_dataset_from_directory(
        train_dir,  # 폴더를 지정한다.
        validation_split=0.2,   # 훈련셋을 훈련셋과 검증셋으로 8:2구조로 나눠서 검증
        seed=123,
        subset="training",
        image_size=(180, 180),
        batch_size=16
    )

    val_ds = keras.utils.image_dataset_from_directory(
        train_dir,  # 폴더를 지정한다.
        validation_split=0.2,   # 훈련셋을 훈련셋과 검증셋으로 8:2구조로 나눠서 검증
        seed=123,
        subset="validation",
        image_size=(180, 180),
        batch_size=16
    )

    model.fit(train_ds, 
              validation_data=val_ds,
              epochs=30 )
    
    model.save("cat_and_dog.keras")     # 모델 저장하기

deeplearning()






