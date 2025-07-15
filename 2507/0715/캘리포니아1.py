import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC     # 서포트벡터머신. 하이퍼파라미터 개수가 많아서 선택함
from sklearn.metrics import classification_report, accuracy_score
import optuna
# classification_report: 분류 중에서도 이진분류 평가 라이브러리
# accuracy_score: 단순히 정확도 판단기준
# GridSearchCV: 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려본다.

cali = fetch_california_housing()
# iris.data, iris.target: numpy배열 => 데이터프레임으로
X = pd.DataFrame(cali.data, columns=cali.feature_names)
y = cali.target     # 0이 악성, 1이 양성  =>  둘의 값을 반전하자. 나중에 모델 평가 해석시에 그게 더 편함


# MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude
print("캘리포니아 집값 정보 :")
print(f"특성개수 {X.shape[1]}")
print(f"샘플개수 {X.shape[0]}")

# 악성인 사람과 양성인 사람간의 데이터 불균형.
# iris는 균형 데이터. 33 : 33 : 33
# 불균형 데이터셋일 경우에 훈련셋과 테스트셋을 쪼갤 때 그 균형을 유지하면서 쪼개라.
# stratify=y_change
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234,
                                                    test_size=0.2)

# # 라이브러리 경향이: 콜백함수를 만들어서 파라미터로 전달해주면 된다.
# # 옵투나가 호출할 콜백함수를 만들어야 한다.
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def objective(trial):   # 변수명은 마음대로
    # 옵투나를 통해 탐색할 하이퍼파라미터 범위를 정의한다.
    # 트리 최대깊이
    max_depth = trial.suggest_int('max_depth', 5, 20)   # 그리드서치 5,6,7,8,...,20  => 옵투나는 시작, 엔딩
    # 리프노드가 되기 위한 최소 샘플수
    min_samples_leaf = trial.suggest_int('min_samples_leaf', 2, 10)
    
    min_samples_split = trial.suggest_int('min_samples_split', 2, 10)
    n_estimators = trial.suggest_int('n_estimators', 2, 10)
    
    model = RandomForestRegressor(max_depth=max_depth, min_samples_leaf=min_samples_leaf,
                                   min_samples_split=min_samples_split, n_estimators=n_estimators,
                                   random_state=42,
                                   n_jobs=-1)   # 내부 프로세스. cpu개수*2 라서 -1을 주면 알아서 최대치를 사용한다.

    pipeline = Pipeline(
        [
            ('scaler', StandardScaler()),
            ('classifier', model)
        ]
    )

    param_grid = {
        'scaler':[StandardScaler(), MinMaxScaler()],
        #'classifier__C':[0.01, 0.1, 10, 100],
        #'classifier__solver':['liblinear', 'lbfgs']
    }

    # 3. 그리드서치 만들기
    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv= 5,
        scoring= 'r2',
        n_jobs=-1,  
        verbose=2,  
    )

    grid_search.fit(X_train, y_train)
    return grid_search.best_score_     # 반드시 마지막에 리턴해야 한다. 목적값

# 옵투나 스터디 생성
study = optuna.create_study(direction="maximize")   # mode = RandomForest()
# 이익을 최대화 하는 방향으로 study객체를 만든다.
print("옵투나 최적화 시작(50회 시도)")
study.optimize(objective, n_trials=50)  # 콜백함수, 횟수를 지정한다.
# optimize - 최적화 함수
print(f"최고 정확도: {study.best_trial.value}")
print(f"하이퍼파라미터: {study.best_trial.params}")



