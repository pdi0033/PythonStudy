url = "https://lib.stat.cmu.edu/datasets/boston"
# 다중회귀분석: 공분산(특성간에 서로 영향을 주고받는것)을 따져보고 필요없는 특성은 제거하는게 맞다.
# R은 기본적으로 제거해준다. 파이썬은 우리가 해야한다.
import pandas as pd     # 다양한 유형의 있을 때 처리 방법
import numpy as np
# 분리문자가 공백이 아니고 \s+, skpirows=22줄 건너뛰기. 제목줄이 없다.
df = pd.read_csv(url, sep="\s+", skiprows=22, header=None)
print(df.head(10))

# np에 hstack 함수가 있음, 수평방향으로 배열을 이어붙이는 함수
# 짝수행에 홀수를 갖다가 붙인다.  df.values[::2, :]  0,2,4,6,8, : 전체컬럼
# 홀수행에 앞에 열 2개만 df.values[1::2, :2]
X = np.hstack([df.values[::2, :], df.values[1::2, :2]])
print(X.shape, X[:10])
y = df.values[1::2, 2]      # 이 열이 target
print(y.shape)
# 행의 개수가 같아야 머신러닝 연산을 수행한다. 결과가 입력한 데이터 개수만큼 있어야 한다.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
print("LinearRegression")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

print("기울기들", model.coef_)
print("절편", model.intercept_)
# 선형회귀분석: 다중공선성문제, 여러 특성간에 서로 너무 밀접해서 필요없는 요소들을 고려하지 않는다.
# 특성의 개수가 많을 경우에 처리 능력이 떨어진다.
# 보스톤 주택가격데이터의 특성의 개수는 13개임, 즉 가중치도 13개가 나온다.

# 개선된 모델이 라쏘하고 리지라는 알고리즘이 있다.
# 라쏘는 쓸데없는 계수(기울기들)

from sklearn.linear_model import Ridge
model = Ridge(alpha=10)
model.fit(X_train, y_train)
print("Ridge")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

print("기울기들", model.coef_)
print("절편", model.intercept_)

from sklearn.linear_model import Lasso
model = Lasso(alpha=10)     # 숫자가 커질수록 규제가 커진다.
model.fit(X_train, y_train)
print("Lasso")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))

print("기울기들", model.coef_)
print("절편", model.intercept_)

