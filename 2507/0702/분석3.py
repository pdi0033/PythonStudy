import pandas as pd
import numpy as np

df = pd.read_csv('./data/iris.csv')

# 1) iris 데이터셋에 몇개의 필드가 있고 각 필드의 타입이 무엇인지 확인해 보세요
print(1)
print('컬럼 수:', len(df.columns))
print('컬럼명:', df.columns)
print()

# 2) 맨 앞의 데이터를 7개만 출력해보세요
print(2)
print(df.head(7))
print()

# 3) iris 데이터셋의 통계량을 확인해보세요(평균, 표준편차, 중간값, 사분위수...)
print(3)
print("sepal.length 평균:", df['sepal.length'].mean())
print("sepal.length 최대:", df['sepal.length'].max())
print("sepal.length 최소:", df['sepal.length'].min())
print("sepal.length 중간:", df['sepal.length'].median())
print("sepal.length 분산:", df['sepal.length'].var())
print("sepal.length 표준편차:", df['sepal.length'].std())
print("sepal.length 1사분위수:", df['sepal.length'].quantile(0.25))
print("sepal.length 2사분위수:", df['sepal.length'].quantile(0.5))
print("sepal.length 3사분위수:", df['sepal.length'].quantile(0.75))
print()

# 4) variety 이 Setosa 인 데이터의 통계량을 출력하세요
print(4)
df2 = df[df['variety']=='Setosa']
# print("sepal.length 평균:", df2['sepal.length'].mean())
# print("sepal.length 최대:", df2['sepal.length'].max())
# print("sepal.length 최소:", df2['sepal.length'].min())
# print("sepal.length 중간:", df2['sepal.length'].median())
# print("sepal.length 분산:", df2['sepal.length'].var())
# print("sepal.length 표준편차:", df2['sepal.length'].std())
# print("sepal.length 1사분위수:", df2['sepal.length'].quantile(0.25))
# print("sepal.length 2사분위수:", df2['sepal.length'].quantile(0.5))
# print("sepal.length 3사분위수:", df2['sepal.length'].quantile(0.75))
print(df2.describe)
print()

# 5) 각각 variety가 Setosa, Virginica Versicolor 의 sepal.length 값의 평균값을 출력하시오
print(5)
print("Setosa 평균:", df[df['variety']=='Setosa']['sepal.length'].mean())
print("Virginica 평균:", df[df['variety']=='Virginica']['sepal.length'].mean())
print("Versicolor 평균:", df[df['variety']=='Versicolor']['sepal.length'].mean())
print()

# 6) 꽃의 종류가 Setosa   이면서 sepal.length 길이가 5cm이상인 것의 개수를 출력하시오 
print(6)
df2 = df[ (df['variety'] == 'Setosa') & (df['sepal.length'] >= 5) ]
print(df2.shape[0])
print()



