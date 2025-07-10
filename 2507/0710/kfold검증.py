"""
kfold 검증
과대적합을 막기위한 고민들
훈련셋을 테스셋을 나누고
데이터 전체를
1 2 3 4 5     5개가 한 그룹    	1~4 훈련셋   	5 테스트셋
			         	2~5 훈련셋      	1 테스트셋
				3~5,1 훈련셋   	2 테스트셋
				…
				이것들의 score의 평균값을 내면
검증방법 k-번 접는다.  =>  데이터가 너무 많아지면 문제가 생긴다. Hold out 검증기법(딥러닝)
훈련셋, 검증셋, 테스트셋 으로 나누어서 각자 학습을 해서 결과를 낸다. 데이터가 적을때는 Kfold검증기법을 많이 사용
"""
from sklearn.datasets import load_iris

data = load_iris() #Bunch 라는 클래스 타입 
print(data.keys())

print("타겟이름 ", data['target_names'])
print("파일명 ", data['filename'])
print("데이터설명")
print(data["DESCR"])

#2.데이터를 나누기 
X = data['data']   #ndarray 2차원배열
y = data['target'] #ndarray 1차원배열 

print(X[:10])
print(y)

from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedGroupKFold    # 개선한 버전
from sklearn.tree import DecisionTreeClassifier
train_score = []
test_score = []

kfold = KFold(n_splits=5)   # 몇개로 쪼갤지를 알려준다.
for train_index, test_index in kfold.split(X):
    # print(train_index)      # 데이터를 잘라내야할 인덱스 목록
    # print(test_index)
    X_train = X[train_index]
    y_train = y[train_index]
    X_test = X[test_index]
    y_test = y[test_index]
    # print(y_train)
    # print(y_test)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    train_score.append(model.score(X_train, y_train))
    test_score.append(model.score(X_test, y_test))

print(train_score)
print(test_score)

print(" --------------- StratifiedGroupKFold ----------------")
train_score = []
test_score = []
sfk = StratifiedGroupKFold(n_splits=5)   # 몇개로 쪼갤지를 알려준다.
# split에 y값도 주면 섞어서 쪼개준다. 분류문제일 경우에 불균등 분할을  =>  균등분할로 바꾸는 역할을 한다.
for train_index, test_index in kfold.split(X, y):
    # print(train_index)      # 데이터를 잘라내야할 인덱스 목록
    # print(test_index)
    X_train = X[train_index]
    y_train = y[train_index]
    X_test = X[test_index]
    y_test = y[test_index]
    # print(y_train)
    # print(y_test)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    train_score.append(model.score(X_train, y_train))
    test_score.append(model.score(X_test, y_test))

print(train_score)
print(test_score)

# score_val_score: 교차 검증에 사용되는 함수
from sklearn.model_selection import cross_val_score
model = DecisionTreeClassifier()
result = cross_val_score(model, X, y, scoring="accuracy", cv=5)
# 정밀도로 하자 cv=5 몇번 접을꺼냐
print(result)
