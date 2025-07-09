import pandas as pd
import numpy as np
df = pd.read_csv("../data/penguins.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# 라벨인코딩 작업
df.loc[df["island"] == "Torgersen", "island"] = 1
df.loc[df["island"] == "Dream", "island"] = 2
df.loc[df["island"] == "Biscoe", "island"] = 3

df.loc[df["sex"] == "MALE", "sex"] = 1
df.loc[df["sex"] == "FEMALE", "sex"] = 2
# map과 유사하게 apply, 함수만들어서 모든 요소한테 그 함수를 적용해라

# 결측치제거
print(df.isnull().sum())
# 결측치 - 제거, 대부분의 경우는 제거보다는 다른값으로 대체하는 경우가 많다.
df = df.dropna(how='any', axis=0)   # NaN 값이 있는 행은 모두 삭제해라
print(df.isnull().sum())
print(df.shape)

X = df.iloc[:, 1:]      # 전체행, 나머지가 입력데이터, 특성, 픽처
y = df.iloc[:, 0]       # 0번열이 목표치 라벨
print(X[:4])
print(y[:4])

# 이상치제거

# 스케일링(정규화, 표준화) - 서포트벡터머신, 딥러닝은 반드시 해줘야한다.
def nor(colName):
    X[colName] = (X[colName] - X[colName].min()) / (X[colName].max() - X[colName].min())
    return X[colName]

nor('bill_length_mm')
nor('bill_depth_mm')
nor('flipper_length_mm')
nor('body_mass_g')
print(X[:4])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))






