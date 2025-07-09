from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer.keys())
X = cancer['data']
y = cancer['target']

from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler, Normalizer
ss = StandardScaler()       # 객체 생성
X_scaled = ss.fit_transform(X)    # 학습하고 바로 변경된 값 반환
print(X_scaled)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

"""
서포트벡터머신
대부분의 머신러닝 알고리즘은 평면에 선을 긋는다.
데이터에 따라서는 평면에 선을 못 긋는 경우에
수학자 차원을 분리시켜서 평면의 다차원공간으로 보내서 차원간에 선을 긋는다.
"""
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("-------- 로지스틱 ----------")
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

from sklearn.svm import SVC
model = SVC()   # 분류
model.fit(X_train, y_train)
print("-------- 스케일링 안한 서포트벡터머신 ----------")
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

print()
print("-------- 스케일링된 서포트벡터머신 ----------")
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(
    X_scaled, y, random_state=0)
model.fit(X_train_scaled, y_train_scaled)
print("훈련셋", model.score(X_train_scaled, y_train_scaled))
print("테스트셋", model.score(X_test_scaled, y_test_scaled))
