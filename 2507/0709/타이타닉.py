# 타이타닉 데이터
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/train_and_test2.csv")
print(df.head())
print(df.columns)
print(df.info())
# ['Passengerid', 'Age', 'Fare', 'Sex', 'sibsp', 'Parch', 'Embarked', 'survived']
# print(df['Parch'].unique())
df.drop('Passengerid', axis=1, inplace=True)

# 1. 결측치
df = df.dropna(how='any', axis=0)
print(df.shape)

# 2. 이상치 처리
def outfliers_iqr(columns_name):    # 이 함수는 이상치의 하한과 상한을 반환한다.
    for cn in columns_name:
        q1, q3 = np.percentile(df[cn], [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - iqr*1.5
        upper_bound = q3 + iqr*1.5
        df[cn] = np.where(df[cn] < lower_bound, lower_bound, df[cn])
        df[cn] = np.where(df[cn] > upper_bound, upper_bound, df[cn])


columns_name = list(df.columns)
outfliers_iqr(columns_name)


# 원핫 인코딩
df_onehot = pd.get_dummies(df, columns=['Sex', 'sibsp', 'Parch', 'Embarked'])
X = df_onehot.iloc[:, :6]
y = df_onehot.iloc[:, 6]    # survived

# 3. 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()       # 객체 생성
X_scaled = ss.fit_transform(X)    # 학습하고 바로 변경된 값 반환

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=0)

# 4. 서포트벡터머신
from sklearn.svm import SVC
model = SVC()   # 분류
model.fit(X_train, y_train)
print("-------- 서포트벡터머신 ----------")
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

