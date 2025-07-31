import re   # 정규식 처리
import string
import tensorflow as tf
from keras.layers import TextVectorization

def custom_standardizaton_fn(text):
    lower_text = tf.strings.lower(text)
    return tf.strings.regex_replace(lower_text, f"[{re.escape(string.punctuation)}]", "")

def cutom_split_fn(text):
    return tf.strings.split(text)

text_vectorization = TextVectorization(
    output_mode= "int",     # 출력이 시퀀스임
    standardize= custom_standardizaton_fn,  # 표준화에 사용할 함수를 전달할 수 있다.
    split= cutom_split_fn,                  # 토큰화에 사용할 함수를 전달할 수 있다.
)

dataset = [
    "I write, erase, reqrite",
    "Erase again, and then",
    "A poppy blooms",
    "Dog is pretty"
]

text_vectorization.adapt(dataset)   # 학습시킬 데이터가 있으면 adapt에 전달하면 된다.

vocabulary = text_vectorization.get_vocabulary()
# 알아서 단어 빈도수로 정리됨
print(vocabulary)

# 인코딩
text = "I write, rewrite, and still rewrite again"
encoded = text_vectorization(text)
print(encoded)

# 디코딩
decoded_voca = dict(enumerate(vocabulary))
print(decoded_voca)

decoded_sen = " ".join(decoded_voca[int(i)] for i in encoded)
print(decoded_sen)
