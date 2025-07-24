"""
사전학습된 모델을 가져다 사용하기
특성추출
CNN하고 완전 피드포워딩         합성곱신경망(CNN) + 완전피드 포워딩
이미 학습된 모델을 불러와서 CNN파트랑 완전연결망을 쪼개서
CNN으로부터 특성을 추출한 다음에 완전연결망한테 보내서 다시 학습(분류학습)을 한다.
CNN이 시간이 많이 걸린다. => CNN재활용을 하면 학습시간도 적게 걸리고, 예측률도 더 높아진다.
이미 수십만장의 사진을 가지고 학습한 모델을 갖다 쓴다.

장점: 데이터셋이 적을 경우(1000장)
	이미 학습된 모델을 사용함으로써 학습시간을 줄여준다.
	컴퓨터 자원이 작아도 학습이 가능하다.
VGG19, ResNet, MobileLet 등 이미지셋 모델들이 있다.

# https://hwanny-yy.tistory.com/11
"""
import gdown    # 케라스 만든 사람들이 케라스에 있는 데이터셋 업어오기 위해 사용함.
# gdown.download(id='18uC7WTuEXKJDDxbj-Jq6EjzpFrgE7IAd', output='dogs-vs-cats.zip')

# VGG19
import os, shutil, pathlib
import tensorflow as tf
import keras
from keras.utils import image_dataset_from_directory
original_dir = pathlib.Path("../../data/dogs-vs-cats/train")
new_base_dir = pathlib.Path("../../data/dogs-vs-cats/dosg-vs-cats_small")

# 폴더로 옮기기
def copyImage():
    def make_subset(subset_name, start_index, end_index):   # make_subset("train", 0, 1000)
        for category in ("cat", "dog"):
            dir = new_base_dir/subset_name/category
            os.makedirs(dir, exist_ok=True)     # 디렉토리가 없을 경우 새로 디렉토리를 만들어라
            fnames = [f"{category}.{i}.jpg" for i in range(start_index, end_index)]
            for fname in fnames:
                shutil.copyfile(src=original_dir/fname, dst=dir/fname)

    make_subset("train", 0, 1000)
    make_subset("validation", 1000, 1500)
    make_subset("test", 1500, 2000)


train_ds = image_dataset_from_directory(
    new_base_dir/"train",
    image_size=(180, 180),
    batch_size=16
)

validation_ds = image_dataset_from_directory(
    new_base_dir/"validation",
    image_size=(180, 180),
    batch_size=16
)

test_ds = image_dataset_from_directory(
    new_base_dir/"test",
    image_size=(180, 180),
    batch_size=16
)

# VGG19 이미지 모델 가져오기
from keras.applications.vgg19 import VGG19
conv_base = keras.applications.vgg19.VGG19(
    weights="imagenet",
    include_top=False,  # CNN만 가져와라, CNN이 하단에 있음
    input_shape=(180, 180, 3),  # 입력할 데이터 크기를 줘야 한다.
    # 데이터셋에서 지정한 크기와 일치해야 한다.
)

conv_base.summary() # CNN요약 확인하기.
# block5_pool (MaxPooling2D)  (None, 5, 5, 512)  0 

# 데이터셋을 주고 CNN으로부터 특징을 추출해서 전달하는 함수
import matplotlib.pyplot as plt
import numpy as np
def get_features_and_labels(dataset):
    all_features = []
    all_labels = []
    for images, labels in dataset:      # 예측할 때처럼 폴더로부터 16개의 이미지와 라벨을 가져온다.
        preprocessed_images = keras.applications.vgg19.preprocess_input(images)
        print(images.shape, preprocessed_images.shape)
        # plt.show()
        # break
        features = conv_base.predict(preprocessed_images)
        all_features.append(features)
        all_labels.append(labels)
    return np.concatenate(all_features), np.concatenate(all_labels)

import pickle
def save_features():
    train_features, train_labels = get_features_and_labels(train_ds)
    validation_features, validation_labels = get_features_and_labels(validation_ds)
    test_features, test_labels = get_features_and_labels(test_ds)

    # 히스토리 저장하기
    features = {"train_features":train_features, "train_labels":train_labels,
                "validation_features":validation_features, "validation_labels":validation_labels,
                "test_features":test_features, "test_labels":test_labels}
    try:
        with open("개와고양이_특성.bin", 'wb') as file:
            pickle.dump(features, file)
        print("개와고양이_특성 저장 완료")
    except Exception as e:
        print(f"개와고양이_특성 저장 중 오류 발생 {e}")

def load_features():
    try:
        with open("개와고양이_특성.bin", 'rb') as file:
            features = pickle.load(file)
            print("개와고양이_특성 로딩 성공")
    except Exception as e:
        print(f"개와고양이_특성 로딩중 실패 : {e}")

    return features


from keras import models, layers
def deeplearning():
    # 특성 추출, 불러오기, 예측
    features = load_features()

    data_argumentation = keras.Sequential([
        layers.RandomFlip("horizontal"), # 이미지를 수평으로 무작위로 뒤집습니다.
        layers.RandomRotation(0.1),     # 이미지를 최대 2pi 라디안의 10(즉, 36도)까지 무작위로 회전시킵니다.
        layers.RandomZoom(0.1),         # 이미지를 최대 10%까지 무작위로 확대하거나 축소합니다.
    ])

    # 맨 마지막 block
    inputs = keras.Input(shape=(5,5,512))
    x = data_argumentation(inputs)
    x = layers.Flatten()(x)
    x = layers.Dense(256)(x)
    x = layers.Dense(128)(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(1, activation='sigmoid')(x)
    model = keras.Model(inputs, outputs)
    # 학습이 과소가 되었던 과대가 되었던 학습이 끝나야 저장이 되는데 
    # 과대적합이 되는 시점에서 저장을 할 수 있다.
    # model이 학습하는 도중에 과대적합이 되는 걸 확인할 수 있다.
    # 콜백함수에 저장할 파일명을 전달하면 자동으로 호출을 한다.
    # list 형태로 받아간다.
    callbacks = [
        keras.callbacks.ModelCheckpoint(
            filepath="특성추출.keras",
            save_best_only=True,    # 가장 적합할 때 저장하기
            monitor="val_loss"      # 검증데이터의 손실 로스 값이 최적화일 떄
        )
    ]
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    
    history = model.fit(features["train_features"], features["train_labels"],
                        epochs=30,
                        validation_data=(features["validation_features"], features["validation_labels"]),
                        callbacks=callbacks)
    
    # 모델 저장하기
    try:
        model.save("dog_vs_cat.keras")     # 모델 저장하기
        print("모델 저장 완료")
    except Exception as e:
        print(f"모델 저장 중 오류 발생 {e}")
    
    # 히스토리 저장하기
    try:
        with open("dog_vs_cat.bin", 'wb') as file:
            pickle.dump(history.history, file)
        print("히스토리 저장 완료")
    except Exception as e:
        print(f"히스토리 저장 중 오류 발생 {e}")

def predict():
    # 1. 학습된 모듈을 불러온다.
    loaded_model_keras = None
    try:
        loaded_model_keras = keras.models.load_model("특성추출.keras")
        print("모델 부르기 성공")
    except Exception as e:
        print(f"모델 로딩중 실패 : {e}")
        return
    
    features = load_features()
    test_features, test_labels = features["test_features"], features["test_labels"]

    # val_ds가 폴더로부터 이미지 파일을 읽어오는데 batch_size만큼씩 읽어온다.
    total_samples_proceed = len(test_labels)
    
    # 예측하기
    predictions_batch = loaded_model_keras.predict(test_features, verbose=2)
    predicted_class = (predictions_batch > 0.5).astype(int).flatten()   # 0.5보다 큰 거는 True, 작은 거는 False

    total_match_count = np.sum(predicted_class == test_labels)
    
    # print(total_samples_proceed, len(labels_batch))
    print("전체 데이터 개수:", total_samples_proceed)
    print("맞춘 개수:", total_match_count)
    print("틀린 개수:", total_samples_proceed - total_match_count)

def main():
    while True:
        print("1. 파일복사")
        print("2. 특성저장")
        print("3. 학습")
        print("4. 예측")
        sel = input("선택 >> ")
        if sel == "1":
            copyImage()
        elif sel == "2":
            save_features()
        elif sel == "3":
            deeplearning()
        elif sel == "4":
            predict()
        else:
            break

if __name__ == "__main__":
    main()