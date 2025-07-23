"""
사전학습된 모델을 가져다 사용하기
특성추출
CNN하고 완전 피드포워딩
이미 학습된 모델을 불러와서 CNN파트랑 완전연결망을 쪼개서
CNN으로부터 특성을 추출한 다음에 완전연결망한테 보내서 다시 학습을 한다.
CNN이 시간이 많이 걸린다. => CNN재활용을 하면 학습시간도 적게 걸리고, 예측률도 더 높아진다.
이미 수십만장의 사진을 가지고 학습한 모델을 갖다 쓴다.

장점: 데이터셋이 적을 경우(1000장)
	이미 학습된 모델을 사용함으로써 학습시간을 줄여준다.
	컴퓨터 자원이 작아도 학습이 가능하다.
VGG19, ResNet, MobileLet 등 이미지셋 모델들이 있다.
"""
import gdown
# gdown.download(id='18uC7WTuEXKJDDxbj-Jq6EjzpFrgE7IAd', output='dogs-vs-cats.zip')

# VGG19
import os, shutil, pathlib
import tensorflow as tf
import keras
original_dir = pathlib.Path("../../data/dogs-vs-cats/train")
new_base_dir = pathlib.Path("../../data/dogs-vs-cats/dosg-vs-cats_small")

# 폴더로 옮기기
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

from keras.utils import image_dataset_from_directory
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
def get_features_and_labels(dataset):
    all_features = []
    all_labels = []
    for images, labels in dataset:      # 예측할 때처럼 폴더로부터 16개의 이미지와 라벨을 가져온다.
        preprocessed_images = keras.applications.vgg19.preprocess_input(images)
        print(images.shape, preprocessed_images.shape)
        plt.show()
        break

get_features_and_labels(train_ds)
