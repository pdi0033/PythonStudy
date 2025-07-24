# 꽃 숫자 세기

import os
base_path = "../../data/flowers"
# print(len(os.listdir(base_path + "/daisy")))
# print(len(os.listdir(base_path + "/dandelion")))
# print(len(os.listdir(base_path + "/sunflower")))
# print(len(os.listdir(base_path + "/rose")))
# print(len(os.listdir(base_path + "/tulip")))

import shutil, pathlib
import tensorflow as tf
import keras
from keras.utils import image_dataset_from_directory
import pickle
from keras import models, layers
import numpy as np
import matplotlib.pyplot as plt

original_dir = pathlib.Path("../../data/flowers")
new_base_dir = pathlib.Path("../../data/flowers_small")
flower_names = ["daisy", "dandelion", "sunflower", "rose", "tulip"]

def make_subset(subset_name, start_index=0, end_index=700):   # make_subset("train", 0, 1000)
    for category in flower_names:
        dir = new_base_dir/subset_name/category     # WindowsPath 라는 특별한 객체, str 아님.
        os.makedirs(dir, exist_ok=True)     # 디렉토리가 없을 경우 새로 디렉토리를 만들어라
        dataList = os.listdir(base_path + '/' + category)
        if end_index != -1:
            fnames = dataList[start_index:end_index]
        else:
            fnames = dataList[start_index:]
        for fname in fnames:
            shutil.copyfile(src=original_dir/category/fname, dst=dir/fname)

# 데이터가 적어서 700건까지만 훈련셋으로 함
def copyImage():
    make_subset("train", 0, 700)
    make_subset("test", 700, -1)    # 700건 이후 나머지 데이터를 테스트셋으로 보냄
    # make_subset("validation", 700, -1)

copyImage()

print(new_base_dir)     # 트레인에 있는 데이터를 훈련셋과 검증셋으로 쪼갰음.
# 데이터가 많지 않아서 검증 폴더를 따로 쪼갤 수 없을 때
train_ds = image_dataset_from_directory(
    new_base_dir/"train",
    seed=1234,              # 동일하게 자르게 하기 위해서
    subset="training",      # 훈련셋
    validation_split=0.2,   # 얼마만큼의 비율로 자를 거냐
    image_size=(180, 180),
    batch_size=16
)

validation_ds = image_dataset_from_directory(
    new_base_dir/"train",
    seed=1234,              # 동일하게 자르게 하기 위해서
    subset="validation",      # 훈련셋
    validation_split=0.2, 
    image_size=(180, 180),
    batch_size=16
)

# VGG19 이미지 모델 가져오기
from keras.applications.vgg19 import VGG19

def deeplearning():
    conv_base = keras.applications.vgg19.VGG19(
        weights="imagenet",
        include_top=False,  # CNN만 가져와라, CNN이 하단에 있음. 상단-완전연결망(분류)
        input_shape=(180, 180, 3),  # 입력할 데이터 크기를 줘야 한다. 뒤이 3은 색깔정보
        # 데이터셋에서 지정한 크기와 일치해야 한다.
    )

    conv_base.summary() # CNN요약 확인하기.
    # block5_pool (MaxPooling2D)  (None, 5, 5, 512)  0 

    conv_base.trainable = True
    print("합성공 기반 층을 동결하기 전의 훈련 가능한 가중치 개수 ", len(conv_base.trainable_weights))
    conv_base.trainable = False     # 동결
    print("합성공 기반 층을 동결하기 후의 훈련 가능한 가중치 개수 ", len(conv_base.trainable_weights))

    # 데이터 증강에 필요한 파라미터들
    data_argumentation = keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.4)
    ])

    # 모델 만들기
    inputs = keras.Input(shape=(180, 180, 3))   # 모델의 입력레이어 정의
    x = data_argumentation(inputs)      # 입력이미지에 데이터 증강을 적용한다.
    x = keras.applications.vgg19.preprocess_input(x)    # vgg19에 맞는 전처리작업(픽셀값범위조정 등)

    # 인라인 방식으로 cnn 연결하기
    x = conv_base(x)    # 특성추출이 이뤄진다. 오래걸린다.
    ###########################################
    x = layers.Flatten()(x)
    x = layers.Dense(256)(x)
    x = layers.Dense(128)(x)
    x = layers.Dense(64)(x)
    outputs = layers.Dense(5, activation='softmax')(x)

    model = keras.Model(inputs, outputs)
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    # 시스템이 내부적으로 일 처리하고 일 끝나면 우리가 전달해준 콜백 함수를 호출한다.
    callbacks = [
        keras.callbacks.ModelCheckpoint(
            filepath='꽃분류_사전학습2.keras',
            save_best_only=True,
            monitor='val_loss',     # 검증 데이터 셋을 기준으로 하겠다. 가장 적절한 시점에 호출할 거다.
        )
    ]

    history = model.fit(train_ds, 
                        epochs=5, 
                        validation_data=validation_ds,
                        callbacks=callbacks)
    
    with open("꽃분류_사전학습2.bin", "wb") as file:
        pickle.dump(history.history, file)



if __name__ == "__main__":
    # make_subset()
    deeplearning()