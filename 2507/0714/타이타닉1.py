"""
1. 'PassengerId', 'Name', 'SibSp', 'Parch' 지우기
2. 각 필드별 결측치 확인
    결측치를 열을 제거하거나 행을 제거할 수도 있다.
    혹은 지나치게 결측치가 많을 경우에는 대체값(평균, 중간(비범주형일 때는 평균 또는 중간값), 최빈값(데이터가 범주형일 때))
3. 이상치 제거
4. 충복값 제거
5. 데이터 자체가 잘못 들어온 값
    value_counts 함수나 Unique로 체크하기
    값 바꾸기를 시도하거나 행을 삭제
6. 라벨링 또는 원핫인코딩
7. 스케일링
8. 학습하고 특성의 개수가 많을 경우는 특성의 중요도 확인
9. 주성분분석
10. 여러가지 모델로 학습하기, GridSearchCV 사용도 가능
"""

# 타이타닉 데이터
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC     # 서포트벡터머신. 하이퍼파라미터 개수가 많아서 선택함
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

df = pd.read_csv("../data/titanic2/train.csv")

# [PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked]
# print(df['Parch'].unique())
df.drop(['PassengerId', 'Name', 'Ticket', 'SibSp', 'Parch'], axis=1, inplace=True)
# [Survived, Pclass, Sex, Age, Fare, Embarked]

# 2. 결측치
df['Age'].fillna(df['Age'].median(), inplace=True)     # Age는 중앙값으로 대체
df.drop('Cabin', axis=1, inplace=True)          # Cabin의 반이상이 결측치라 그냥 날림
mode_embarked = df['Embarked'].mode()[0]  # 가장 첫 번째 최빈값 선택
df['Embarked'].fillna(mode_embarked, inplace=True) 
# print("대체 후 데이터프레임 NaN수")
# print(df.isna().sum())
print(df.head())

# 3. 이상치 처리
def outfliers_iqr(columns_name):    # 이 함수는 이상치의 하한과 상한을 반환한다.
    q1, q3 = np.percentile(df[columns_name], [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - iqr*1.5
    upper_bound = q3 + iqr*1.5
    outliers_count = df[columns_name][(df[columns_name] < lower_bound) | (df[columns_name] > upper_bound)].count()
    print(f"{columns_name} 컬럼의 이상치 개수: {outliers_count}개")
    df[columns_name] = np.where(df[columns_name] < lower_bound, lower_bound, df[columns_name])
    df[columns_name] = np.where(df[columns_name] > upper_bound, upper_bound, df[columns_name])

outfliers_iqr('Fare')


# 4. 중복값 제거
print("중복된 데이터")
col = df.duplicated()     # True나 False의 리스트로 보여준다.
print(df[col])

# print("중복 삭제 후")
# df2 = df.drop_duplicates()      # 삭제된 데이터를 반환. 전체필드가 완전히 일치하는 데이터만 삭제한다.
# print(df2)

# 5. 잘못된 값이 있는지 확인. 없는듯ㄴ
# for cn in list(df.columns):
#     print(df[cn].value_counts())

# 6. 원핫 인코딩
df = pd.get_dummies(df, columns=['Sex', 'Embarked'])

# 7. 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print(df.head())

# 8. 학습하고 특성의 개수가 많을 경우는 특성의 중요도 확인
# [Survived, Pclass, Sex, Age, Fare, Embarked]
X = df.iloc[:, 1:]
y = df.iloc[:, 0]
print(X[:2])
print(y[:2])

# 9. 주성분분석
from sklearn.decomposition import PCA
pca = PCA(n_components=16)   # 성분개수 지정하기
pca.fit(X)       # 학습
X_pca = pca.transform(X)

# 10. 여러가지 모델로 학습하기, GridSearchCV 사용도 가능
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, random_state=0)

# 파라미터 설정하기
param_grid = {
    'svc': {
        'C': [0.1, 1, 10, 100],     # 오차허용범위를 조절한다. 내부적으로 오차를 조율하는데 이 값 범위내에서 움직임
                                    # 값이 크면 과대적합 위험
        'gamma': [1, 0.1, 0.01, 0.001], # 커널의 영향 범위, 클수록 과대적합 위험
        'kernel': ['rbf', 'linear'],    # 비선형(데이터가 비선형일 때 좋음), 선형구조(데이터가 선형일 때)
    },
    'random_forest': {
        'n_estimators':[50, 100, 200],   # 트리를 여러 개 만든다. 50, 100, 200 개 만들어봐라
        'max_depth': [None, 3, 10, 20], # 최대깊이
        'min_samples_split': [2, 5, 10] # 가지치기 개수
    },
    'gradient_boosting': {
        'n_estimators':[50, 100, 200],   # 트리를 여러 개 만든다. 50, 100, 200 개 만들어봐라
        'max_depth': [None, 3, 10, 20], # 최대깊이
        'learning_rate': [0.01, 0.1, 0.2]   # 학습률
    }
}

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
results = {}
models = {
    'svc':SVC(),
    'random_forest': RandomForestClassifier(random_state=42),
    'gradient_boosting': GradientBoostingClassifier(random_state=42)
}

#모델에 저장된요소마다 파라미터를 이용해 적용해 본다. 
for model_name, model in models.items():
    print(f"Running GridSearchCV for {model_name}...")
    grid = GridSearchCV(estimator=model, 
                        param_grid=param_grid[model_name], cv=5, verbose=2, scoring='accuracy')
    grid.fit(X_train, y_train)
    results[model_name] = {
        'best_params': grid.best_params_,
        'best_score': grid.best_score_,
        'best_model': grid.best_estimator_
    }

# 4. 테스트 데이터에 대한 성능 평가
for model_name, result in results.items():
    print(f"\nModel: {model_name}")
    print("Best Parameters:", result['best_params'])
    print("Best Cross-Validation Score:", result['best_score'])
    
    # 테스트 데이터로 예측
    y_pred = result['best_model'].predict(X_test)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("Test Set Accuracy:", accuracy_score(y_test, y_pred))

