import pandas as pd
import numpy as np
df = pd.read_csv("../data/diamonds.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# 결측치제거
# print(df.isnull().sum())
# 결측치 - 제거, 대부분의 경우는 제거보다는 다른값으로 대체하는 경우가 많다.
df = df.dropna(how='any', axis=0)   # NaN 값이 있는 행은 모두 삭제해라
# print(df.isnull().sum())
print(df.shape)

# 라벨인코딩 작업
df_onehot = pd.get_dummies(df, columns=['color', 'clarity'])
# df_onehot.loc[df_onehot['cut'] == "Fair", "cut"] = 1
# df_onehot.loc[df_onehot['cut'] == "Good", "cut"] = 2
# df_onehot.loc[df_onehot['cut'] == "Very Good", "cut"] = 3
# df_onehot.loc[df_onehot['cut'] == "Premium", "cut"] = 4
# df_onehot.loc[df_onehot['cut'] == "Ideal", "cut"] = 5
# print(df_onehot.head())

# 스케일링(정규화, 표준화) - 서포트벡터머신, 딥러닝은 반드시 해줘야한다.
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
num_cols = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
df_onehot[num_cols] = scaler.fit_transform(df_onehot[num_cols])
print(df_onehot.head())

X = df_onehot.drop(df_onehot.columns[1], axis=1)      # 전체행, 나머지가 입력데이터, 특성, 픽처
y = df_onehot.iloc[:, 1]       # 0번열이 목표치 라벨
print(X[:4])
print(y[:4])

# 이상치제거


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

