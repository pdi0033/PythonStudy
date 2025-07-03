import pandas as pd
import numpy as np

df = pd.read_csv('../data/iris_ex.csv')
print(df.info())
print(df.head())

# 1. data폴더내의 iris.csv파일을 읽어서, 누락된 데이터가 어떤 필드에 몇개 있는지 찾아내세요 
print(df.isnull().sum())

# 2. 누락된 데이터들을 평균치로 대체하세요
sl_mean = df['sepal.length'].mean()
sw_mean = df['sepal.width'].mean()
pl_mean = df['petal.length'].mean()
pw_mean = df['petal.width'].mean()

df['sepal.length'].fillna(sl_mean, inplace=True)
df['sepal.width'].fillna(sw_mean, inplace=True)
df['petal.length'].fillna(pl_mean, inplace=True)
df['petal.width'].fillna(pw_mean, inplace=True)
print(df.isnull().sum())

# 3. sepal.length, sepal.width, petal.width 세개의 필드에 정규화를 진행하세요 
df['sl_nor'] = (df['sepal.length'] - df['sepal.length'].min()) / (df['sepal.length'].max() - df['sepal.length'].min())
df['sw_nor'] = (df['sepal.width'] - df['sepal.width'].min()) / (df['sepal.width'].max() - df['sepal.width'].min())
df['pw_nor'] = (df['petal.width'] - df['petal.width'].min()) / (df['petal.width'].max() - df['petal.width'].min())
print(df.head())
# 정규화 함수
def normalize(columName):
    max = df[columName].max()
    min = df[columName].min()
    return (df[columName] - min) / (max - min)

df['sl_nor2'] = normalize('sepal.length')
df['sw_nor2'] = normalize('sepal.width')
df['pw_nor2'] = normalize('petal.width')
print(df.head())

# 4. petal.length 필드를 3개의 구간으로 나누어서  A, B, C 이라고 구간 이름을 붙여서 
#  petal_grade 필드를 추가하세요 
count, bin_dividers = np.histogram(df['petal.length'], bins=3)
print('각 구간별 데이터 개수 : ', count)
print('구간 정보 : ', bin_dividers)

bin_names = ["A", "B", "C"]
df['petal_grade'] = pd.cut(x=df['petal.length'], bins=bin_dividers,
                        labels=bin_names, include_lowest=True)
print(df.head())

# 원핫 인코딩으로 전환하세요 
# 카테고리 타입 분석, 분류 분석, 텍스트 분석
# 사이킷런 fit 학습하다. 이차원배열(2d)형태로만 입력을 받는다.
# 새로운 축을 추가해서 1d -> 2d
grade = df['petal_grade']
Y_class = np.array(grade)
Y_class = Y_class.reshape(-1,1)
print(Y_class[:5])

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class)
Y_class_onehot = enc.transform(Y_class).toarray()
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1, 1)
print(Y_class_onehot[:5])
print(Y_class_recovery[:10])

