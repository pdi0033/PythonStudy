import pandas as pd
import numpy as np
df = pd.read_csv("../data/diamonds.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# 1. cut나 clarity의 경우면 분류
# 2.price의 경우는 회귀로
# cut color clarity -> 카테고리화 시켜서 -> 라벨인코딩을 하거나 원핫 인코딩하기
# value_counts() -> 속성하고 개수
print(df['cut'].value_counts())
print(df['color'].value_counts())
print(df['clarity'].value_counts())
print(df['color'].unique())     # 특정 필드에서 값 하나씩만 가져온다.

def getLabelMap(field):
    colorList = df[field].unique()
    # list를 받아와서 map으로 바꾸기
    colorMap = {item: index +1 for index, item in enumerate(colorList)}
    return colorMap

def changeLabeling():
    colorMap = getLabelMap('color')
    df['color_label'] = df['color'].map(colorMap)
    clarityMap = getLabelMap('clarity')
    df['clarity_label'] = df['clarity'].map(clarityMap)
    cutMap = getLabelMap('cut')
    df['cut_label'] = df['cut'].map(cutMap)

changeLabeling()
print(df.head())
print(df.columns)
X = df.loc[:, ['carat', 'depth', 'table', 'price', 'x', 'y',
       'z', 'color_label', 'clarity_label']]
y = df.loc[:, 'cut_label']
print(X[:5])
print(y[:5])


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))