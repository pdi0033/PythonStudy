import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC     # 서포트벡터머신. 하이퍼파라미터 개수가 많아서 선택함
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
# classification_report: 분류 중에서도 이진분류 평가 라이브러리
# accuracy_score: 단순히 정확도 판단기준
# GridSearchCV: 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려본다.

iris = load_breast_cancer()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234)

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
# 1. 파이프라인 구축
pipeline = Pipeline(
    steps=[
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(random_state=42))
    ]
)

# 파이프라인과 그리드서치 간에 파라미터 주는 규칙
# 파이프라인에서 모델 앞에 classifier 주면 매개변수가 C면 
# classifier__C, classifier__solver
# 2. 그리드서치 구축
param_grid = {
    'scaler':[StandardScaler(), MinMaxScaler()],
    'classifier__C':[0.01, 0.1, 10, 100],
    'classifier__solver':['liblinear', 'lbfgs']
}

from sklearn.model_selection import StratifiedKFold
# 3. 그리드서치 만들기
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    # cv에 숫자 5 - Kfold 검증. 타겟이 불균형세트일 때는 아래처럼. 균형유지
    cv= StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    # roc 곡선 -- 암환자같이 잘못 예측한 경우에 위험할 경우, 
    # 데이터 불균형이 클 때 accuracy만으로는 한계가 있다.
    scoring= 'roc_auc',
    n_jobs=-1,  # process개수 최적화
    verbose=2,  # 학습중인 과정을 상세히
)

grid_search.fit(X_train, y_train)

print("최적의 파라미터")
print(grid_search.best_params_)
print("최고점수")
print(grid_search.best_score_)


