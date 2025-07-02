import pandas as pd 

# 분석에서 데이터가 크게 두 종류가 있다.
data = pd.read_csv("./data/auto-mpg.csv")

#value_counts 각 데이터별 고유카운트 - 빈도수, 발생빈도수를 카운트한다.
print( data['model-year'].value_counts()) 

#평균, 최대, 최소 
print("연비평균 : ", data['mpg'].mean())
print("연비최대 : ", data['mpg'].max())
print("연비최소 : ", data['mpg'].min())
print("연비중간 : ", data['mpg'].median())
print("연비분산 : ", data['mpg'].var())
print("연비표준편차 : ", data['mpg'].std())

print("1사분위수 : ", data['mpg'].quantile(0.25))
print("2사분위수 : ", data['mpg'].quantile(0.5))
print("3사분위수 : ", data['mpg'].quantile(0.75))
