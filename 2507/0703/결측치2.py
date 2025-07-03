import pandas as pd
import numpy as np

data = pd.read_csv('../data/data.csv')

print(data.head())
print(data.info())

print('height 결측치: ', data['height'].isnull().sum())
print('weight 결측치: ', data['weight'].isnull().sum())
print('데이터프레임 전체 결측치: ', data.isnull().sum())

mean_height = data['height'].mean()
mean_weight = data['weight'].mean()


data['height'].fillna(mean_height, inplace=True)
data['weight'].fillna(mean_height, inplace=True)

print("누락데이터 교체 후")
print(data.isnull().sum())


