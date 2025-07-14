# ColumnTransformer 라는 클래스가 있따.
# 컬럼단위로 전처리 작업을 해야 할 때 쭈욱 지정해놓으면 이것저것 적용을 해준다.

import mglearn.datasets
import pandas as pd
import mglearn
import os
import matplotlib.pyplot as plt
import numpy as np

names=['age', 'workclass', 'fnlwgt', 'education',  'education-num',
           'marital-status', 'occupation', 'relationship', 'race', 'gender',
           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
           'income']

data = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH, "adult.data"), header=None, index_col=False, names=names)
print(data.head())

# 마지막 필드가 타겟이다.
data = data[ ['age', 'workclass', 'education', 'gender', 'hours-per-week', 'occupation', 'income'] ]
print(data.head())

# get_dummies 함수
# data = pd.get_dummies(data)
# print(data.head())
# print(data.columns)

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

st = ColumnTransformer([
    ("scaling", StandardScaler(), ['age', 'hours-per-week']),
    ("onehot", OneHotEncoder(sparse_output=False), [
        'workclass', 'education', 'gender', 'occupation'
    ])
])

st.fit(data)
print(st.transform(data))

