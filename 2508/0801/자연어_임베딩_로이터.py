import tensorflow as tf
from keras.layers import TextVectorization
import os, pathlib, shutil, random
import keras
import numpy as np

# train => train과 validation으로 나눠야 한다.
# train 폴더에 있는 unsup 폴더는 직접 지워야 한다.

base_dir = pathlib.Path("../../data/reuters")

# 라벨링
def labeling(trte):
    text_dir = base_dir/"r8-train-all-terms.txt"
    if trte == "test":
        text_dir = base_dir/"r8-test-all-terms.txt"

    labels = set()
    with open(text_dir, "r", encoding='utf-8') as f:
        i = 1
        for line in f:  # 한 라인씩 읽기
            word, coefs = line.split(maxsplit=1)
            # print(word)
            # print(coefs)

            word_dir = base_dir/trte/word
            if word not in labels:
                os.makedirs(word_dir)
                labels.add(word)

            with open(word_dir/f"{i}.txt", "w", encoding="utf-8") as wf:
                wf.write(coefs)
            
            i += 1
            
# labeling("train")
# labeling("test")

batch_size = 32     # 한번에 읽어올 양
train_ds = keras.utils.text_dataset_from_directory(
    "../../data/reuters/train",    # 디렉토리명
    batch_size=batch_size
)

test_ds = keras.utils.text_dataset_from_directory(
    "../../data/reuters/test",    # 디렉토리명
    batch_size=batch_size
)

for inputs, targets in train_ds:    # 실제 읽어오는 데이터 확인
    # print("inputs.shape", inputs.shape)
    # print("inputs.dtype", inputs.dtype)
    # print("targets.shape", targets.shape)
    # print("targets.dtype", targets.dtype)
    # print("inputs[0]", inputs[:3])
    # print("targets[0]", targets[:3])
    break

max_length = 600    # 한 평론에서 사용하는 단어는 최대 600개라고 보자
max_tokens = 20000  # 자주 사용하는 단어 2만 개만 쓰겠다.

text_vectorization = TextVectorization(
    max_tokens= max_tokens,
    output_mode= "int",     # 임베딩 층을 사용하려면 반드시 int여야 한다.
    output_sequence_length= max_length,
)

text_only_train_ds = train_ds.map(lambda x, y: x)
text_vectorization.adapt(text_only_train_ds)

int_train_ds = train_ds.map(lambda x,y: (text_vectorization(x), y), num_parallel_calls=1)
int_test_ds = test_ds.map(lambda x,y: (text_vectorization(x), y), num_parallel_calls=1)

# Word2Vec 파일 불러오기
from gensim.models import KeyedVectors
filename = "../../data/Word2Vec/GoogleNews-vectors-negative300.bin"

try:
    word2vec_model = KeyedVectors.load_word2vec_format(filename, binary=True)
    # 파일이 txt 형태가 있고 binary 형태가 있다. binary 형태를 읽겠다.
    embedding_dim = word2vec_model.vector_size
except FileNotFoundError:
    print(filename + "을 찾을 수 없습니다.")
    exit()  # 프로그램 종료
except Exception as e:
    print("에러발생 " + e)
    exit()
print("파일 로딩 성공")

vocabulary = text_vectorization.get_vocabulary()    # 우리 어휘사전 가져오기
word_index = dict(zip(vocabulary, range(len(vocabulary))))
embedding_matrix = np.zeros( (max_tokens, embedding_dim) ) 

for word, i in word_index.items():
    # 단어와 인덱스를 가져온다.
    if i < max_tokens:  # 혹시나 2만 개를 넘어가는 토큰이 있을까봐 오류처리
        try:
            embedding_vector = word2vec_model[word]   # 단어에 해당하는 벡터들 이동
            embedding_matrix[i] = embedding_vector
        except KeyError:
            pass    # 건너뛰기만
    
print(embedding_matrix[:10])

import tensorflow as tf
from keras import models, layers

inputs = keras.Input(shape=(None,), dtype="int64")
embedded = layers.Embedding(
    input_dim= max_tokens, 
    output_dim=embedding_dim,
    embeddings_initializer=keras.initializers.Constant(embedding_matrix),    # 반드시!!!
    # 사전 학습된 층에 의해 바꿔치기가 이뤄져야 한다.
    trainable=False,    # 임베딩 가중치를 훈련 중에 업데이트할 거냐? 사전 학습된 임베딩층을 사용할 떄는 False로 지정해야 한다.
    mask_zero=True,     
    )(inputs)
# 미리 학습된 임베딩층으로 바꿀 수 있다.
# 입력 벡터 크기는 2만, 출력벡터는 256(특별한 의미 없이 마음대로)의 크기를 갖는다.
print(embedded.shape)

# 양방향 RNN을 가동시킴
x = layers.Bidirectional(layers.LSTM(32))(embedded)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(8, activation='softmax')(x)
model = keras.Model(inputs, outputs)
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

callbacks = [
    keras.callbacks.ModelCheckpoint("RNN5.keras", save_best_only=True)
]
model.fit(int_train_ds, validation_data=int_test_ds, epochs=20, callbacks=callbacks)
print("테스트셋:", model.evaluate(int_test_ds))









