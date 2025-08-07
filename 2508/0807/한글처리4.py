# pip install Korpora
# 네이버 영화평을 준다.
from Korpora import Korpora
import tensorflow as tf
import keras
from keras.layers import TextVectorization
from konlpy.tag import Okt
import re
import os, pathlib, shutil, random
import numpy as np # Used for dummy dataset creation
from keras import layers
import pickle

Korpora.fetch("nsmc")
# C:\Users\사용자계정\Korpora\nsmc  : 저장위치
corpus = Korpora.load("nsmc")
print(corpus.train[:3])

# 데이터셋을 사용하기 위해서 해야할 작업
def create_korean_dataset(base_dir="korean_imdb"):
    # 네이버영화평 파일을 읽어서 폴더 나누고 텍스트를 라벨보고 나눠서 넣기
    if os.path.exists(base_dir):    # 이미 폴더가 존재하면 
        try:
            shutil.rmtree(base_dir) # 폴더 삭제
        except OSError as e:
            print("error", e)
    
    # 서브디렉토리를 만들자, train, test, val
    os.makedirs(os.path.join(base_dir, "train", "pos"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "train", "neg"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "val", "pos"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "val", "neg"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "test", "pos"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "test", "neg"), exist_ok=True)

    # 파일은 train 파일과 corpus가 이미 파일을 읽은 상태임, train, test쪽에 데이터가 있음
    pos_train_texts = []
    neg_train_texts = []
    for i in range(len(corpus.train)):
        if corpus.train[i].label == 1:
            pos_train_texts.append(corpus.train[i].text)
        else:
            neg_train_texts.append(corpus.train[i].text)
    
    pos_test_texts = []
    neg_test_texts = []
    for i in range(len(corpus.test)):
        if corpus.test[i].label == 1:
            pos_test_texts.append(corpus.test[i].text)
        else:
            neg_test_texts.append(corpus.test[i].text)

    # 훈련셋을 검증셋과 나누자
    pos_val_texts = pos_train_texts[:1000]
    neg_val_texts = neg_train_texts[:1000]
    
    pos_train_texts = pos_train_texts[1000:]
    neg_train_texts = neg_train_texts[1000:]

    for i, text in enumerate(pos_train_texts):
        with open(os.path.join(base_dir, "train", "pos", f"pos_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)

    for i, text in enumerate(neg_train_texts):
        with open(os.path.join(base_dir, "train", "neg", f"neg_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)
    
    for i, text in enumerate(pos_val_texts):
        with open(os.path.join(base_dir, "val", "pos", f"pos_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)

    for i, text in enumerate(neg_val_texts):
        with open(os.path.join(base_dir, "val", "neg", f"neg_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)

    for i, text in enumerate(pos_test_texts):
        with open(os.path.join(base_dir, "test", "pos", f"pos_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)

    for i, text in enumerate(neg_test_texts):
        with open(os.path.join(base_dir, "test", "neg", f"neg_{i}.txt"), "w", encoding="utf-8-sig") as f:
            f.write(text)

    print("작업완료")
    return base_dir

# 1. 한글 데이터셋을 만들었음.
# korean_data_dir = create_korean_dataset("../../data/korean_imdb")
korean_data_dir = "../../data/korean_imdb"

# 2. 데이터셋을 로드 및 초기화
# keras.utils.text_dataset_from_directory를 사용한다. 데이터를 읽어올 준비, 과정설정
batch_size = 32
train_ds_raw = keras.utils.text_dataset_from_directory(
    korean_data_dir + "/train", batch_size=batch_size, label_mode = "binary"
)
val_ds_raw = keras.utils.text_dataset_from_directory(
    korean_data_dir + "/val", batch_size=batch_size, label_mode = "binary"
)
test_ds_raw = keras.utils.text_dataset_from_directory(
    korean_data_dir + "/test", batch_size=batch_size, label_mode = "binary"
)

#### 한글이나 비영어권 국가들
# 3. 한국어 텍스트 전처리 함수 준비 
okt = Okt()

def clean_text(text):
    #### 이 함수가 호출을 우리가 직접해서 Tensor에 넘겨주는 게 아님
    # train_ds_raw을 이용해서 파일을 읽는건 keras가 읽어서 우리한테 뭐로 주느냐 Tensorflow
    # Tensorflow 용어의 시작은 Tensor(벡터) -> Tensor(벡터)
    # 데이터가 텐서들을 타고 흐른다고 봐서 Tensorflow라고 했음
    # Tensorflow의 Tensor로 준다. 문자셋이 인코딩작업을 거쳐서 전달된다.
    # \U05\u0x  16진수로 바꿔서 온다.
    # 디코딩작업을 반드시 해야 한다.
    text = text.decode("utf-8-sig")     # tf.tensor -> python의 string으로 바뀐다.
    text = text.lower()     # 대문자를 -> 소문자로 바꿔서 처리하자
    text = re.sub(r"[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\s]", "", text)
    return text


# tf.tensor 형태로 데이터를 받아서 => 스트링으로 바꿔서 정규화(쓸데없는 문자들 없애고), 토큰을 나눠서
# tf.tensor로 바꿔야 한다.
def python_korean_preprocess(text_tensor):  # 매개변수의 타입이 tf.tensor타입
    processd_text = []   # 여기에 처리한 문자열을 저장한다.
    for text_bytes in text_tensor.numpy():  # "/u01/u0x ....."
        # 인코딩된 데이터를 전달받는다.
        cleand_text = clean_text(text_bytes)    # tf.tensor => string 으로 받는다.
        morphed_text = " ".join(okt.morphs(cleand_text))
        processd_text.append(morphed_text)
        # list => string  ==>  Tensorflow의 Tensor로 전환해서 보내야 한다.
    
    return tf.constant(processd_text, dtype=tf.string)

def tf_korean_preprocess_fn(texts, labels):
    # tf.py_function 이 함수가 하는 일이 Python 함수를 Tensorflow에 끼워넣는다.
    processed_texts = tf.py_function(
        func= python_korean_preprocess,     # 전달할 함수
        inp=[texts],    # 입력데이터
        Tout=tf.string, # 출력형태
    )
    # 명시적으로 타입을 정해줘야 한다.
    processed_texts.set_shape(texts.get_shape())
    return processed_texts, labels


# TextVectorization을 만들어야 한다. => 어휘사전을 만들어야 한다.
max_tokens = 10000      # 어휘사전은 자주 쓰는 단어 10000 개만
output_sequence = 20    # 문장의 길이를 20개 단어로 제한하겠다.
vectorizer = TextVectorization(
    max_tokens=max_tokens,
    output_mode= "int",     # 반드시 시퀀스를 보내야 함. 꼭 int만 가능하다.
    output_sequence_length=output_sequence,
    standardize=None,       # 따로 표준화를 진행함
    split="whitespace",     # 토큰을 공백을 기준으로 분리한다.
)

# 모든 데이터셋에 대해서 tf_korean_preprocess_fn 함수처리를 해야 한다.
# map 함수는 연산을 수행하여 반환하는 함수이다.
# texts, labels가 있을 때 각 요소를 하나씩 전달 후 연산을 수행해서 반환한다.
# num_paralle_calls=tf.data.AUTOTUNE: 시스템 상태에 따른 적당한 병행처리, 직접 개수를 지정할 수도 있다.
train_ds_processed = train_ds_raw.map(tf_korean_preprocess_fn, num_parallel_calls=tf.data.AUTOTUNE)
val_ds_processed = val_ds_raw.map(tf_korean_preprocess_fn, num_parallel_calls=tf.data.AUTOTUNE)
test_ds_processed = test_ds_raw.map(tf_korean_preprocess_fn, num_parallel_calls=tf.data.AUTOTUNE)
print("전처리 완료")

# 어휘사전 만들기
vectorizer.adapt(train_ds_processed.map(lambda x, y: x))    # x:text, y:label

# 실제 학습을 하려면 우리 데이터를 => 벡터화 시켜야 한다.
def vectorize_text_fn(texts, labels):
    return vectorizer(texts), labels    # 벡터화해서 반환한다.

def study():
    train_ds_vectorized = train_ds_processed.map(vectorize_text_fn, num_parallel_calls=tf.data.AUTOTUNE)
    val_ds_vectorized = val_ds_processed.map(vectorize_text_fn, num_parallel_calls=tf.data.AUTOTUNE)
    test_ds_vectorized = test_ds_processed.map(vectorize_text_fn, num_parallel_calls=tf.data.AUTOTUNE)

    # 데이터셋이 사용하게 cpu임 - 캐쉬랑 프리패치
    train_ds_vectorized = train_ds_vectorized.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds_vectorized = val_ds_vectorized.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    test_ds_vectorized = test_ds_vectorized.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

    # 결과확인
    print(vectorizer.get_vocabulary()[:20])
    for text_batch, label_batch in train_ds_vectorized.take(1):     # 한 사이클만 가져와서
        print(text_batch.shape)
        print(label_batch.shape)
        print(text_batch[0, :10].numpy())

        # 역변환하여 확인해보자
        vocabulary = vectorizer.get_vocabulary()
        decoded = " ".join(vocabulary[idx] for idx in text_batch[0, :10].numpy() if idx>1)
        print(decoded)

    print("준비작업 완료")

    #### 딥러닝: Embeddinf(밀집벡터) -> 단어와 단어 사이의 거리를 표현한다.
                # 원핫인코딩 - 희소행렬, 차원이 너무 거대하다.
    voca_size = vectorizer.vocabulary_size()
    embedding_dim = 128     # 대충, 특별히 사전에 학습된 내용을 사용하는 것이 아니면 차원을 마음대로 줄 수 있다.
    inputs = keras.Input(shape=(None,), dtype=tf.int64)     # 입력층 만들고
    x = layers.Embedding(
        input_dim=voca_size,
        # embedding_initialize는 기본적으로 uniform(랜덤)으로 초기화 학습된 모델을 사용하려면 이 값을 지정해야 한다.
        mask_zero=True,
        output_dim=embedding_dim
    )(inputs)
    x = layers.Bidirectional(layers.LSTM(32))(x)   # 순환신경망
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(1, activation='sigmoid')(x)       # 이진분류라서
    model = keras.Model(inputs, outputs)

    model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=['accuracy'])
    model.summary()

    callbacks = [
        keras.callbacks.ModelCheckpoint("korean_rnn_model.keras", 
                                        save_best_only=True,
                                        monitor="val_accuracy",
                                        mode="max"
                                        )
    ]

    print("\n모델 훈련 시작...")
    history = model.fit(train_ds_vectorized,
                        validation_data=val_ds_vectorized,
                        epochs=5,
                        callbacks=callbacks)
    with open("korean_rnn_history.bin", "wb") as f:
        pickle.dump(history.history, f)
    print("완료")

def predict():
    model = keras.models.load_model("korean_rnn_model.keras")
    with open("korean_rnn_history.bin", "rb") as f:
        history = pickle.load(f)

    sample = [
        "이 영화는 정말 감동적이었어요",
        "영화 수준이 좀 초등학생용 같아요",
        "개연성도 없고 시나리오 발로 썼냐",
        "반드시 봐야할 영화입니다. 인생을 풍요롭게 하는 영화였어요",
        "배우 하나로 이런 영화가 만들어질 수 있다는게 믿기지 않습니다.",
    ]
    
    # 샘플도 클린하게 
    processed_sample = [
        " ".join(okt.morphs(clean_text(text.encode("utf-8-sig")))) for text in sample
    ]

    vectorize_sample = vectorizer(tf.constant(processed_sample, dtype=tf.string))
    prediction = model.predict(vectorize_sample)
    # 확률
    prob = prediction.flatten()
    for i, text in enumerate(sample):
        sentiment = "긍정 " if prob[i] >= 0.5 else "부정"
        print(text[:40], "===> ", sentiment, prob[i])

predict()
