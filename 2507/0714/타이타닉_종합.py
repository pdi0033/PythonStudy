import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier     # 중요도파악
from sklearn.preprocessing import StandardScaler

import os   # 파일이나 폴더경로를 정확하게 지정하려고
train = pd.read_csv("../data/titanic2/train.csv")
test = pd.read_csv("../data/titanic2/test.csv")
print(train.shape)

# 1. 불필요한 열 삭제, Cabin은 결측치가 너무 많아서 제거한다.
print(train.head())     # 원본데이터 inplace=True << 안 먹히는 함수가 많다.
train = train.drop(columns=['PassengerId', 'Name', 'SibSp', 'Parch', 'Cabin'])
test = test.drop(columns=['PassengerId', 'Name', 'SibSp', 'Parch', 'Cabin'])
print(train.head())
print(train.shape)  # 특성 4개 삭제함

# 2. 결측치를 제거
# 1) 결측치 확인
print(train.isna().sum())     # 각 특성별로 결측치가 나옴.
# Age - 177, Cabin - 687, Embarked - 2
# Age나 Embarked는 대체를 
print(train.describe())

# 평균값으로 대체함
age_mean = train['Age'].mean()
train['Age'].fillna(age_mean, inplace=True)     # 자기 자신이 바뀐다.
test['Age'].fillna(age_mean, inplace=True)     # 자기 자신이 바뀐다.
print(train['Age'].isna().sum())
print(train.isna().sum()) 
print(test.isna().sum()) 

# Embarked는 행을 삭제시키자
train = train.dropna(axis=0, how='any')     
# 행 중에 한 컬럼이라도 NaN값이 있으면 전체행을 삭제시켜라.
test = test.dropna(axis=0, how='any')    

# 2. 이상치 제거
# boxplot을 그려보자
# train.boxplot()     # 데이터프레임이 내부적으로 몇 개의 차트는 가지고 있다.
# plt.show()      # 이상치를 확인하기 위해 boxplot을 그려보자

def outfliers_iqr(data):
    q1,q3 = np.percentile(data,[25,75]) #percentile은 값 2개를 넘겨받을수있다
    iqr = q3-q1
    lower_bound = q1 -(iqr*1.5)
    upper_bound = q3 +(iqr*1.5)

    return lower_bound,upper_bound # tuple형태로 두값을 반환

# 두 개의 필드 Fare, Age 필드가 이상치가 발견됨
for i in ['Fare', 'Age']:
    lower, upper = outfliers_iqr(train[i])
    train[i][train[i] < lower] = lower
    train[i][train[i] > upper] = upper

for i in ['Fare', 'Age']:
    lower, upper = outfliers_iqr(test[i])
    test[i][test[i] < lower] = lower
    test[i][test[i] > upper] = upper
    
# train.boxplot()
# plt.show()
# test.boxplot()
# plt.show()

# 3. 원핫인코딩
train = pd.get_dummies(train)
print(train.head())
print(train.columns)


# 산포도행렬이든지 아니면 상관계수
print(train.corr())   # 상관계수를 구할 수 없는 필드들이 있어서 출력 안됨
# import seaborn as sns
# sns.pairplot(train, diag_kind='kde', hue='Survived', palette='bright')
# plt.show()

# Survived가 젤 처음에 있음
X = train.iloc[:, 1:]
y = train.iloc[:, 0]
print(X.shape)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
print(model.score(X, y))


