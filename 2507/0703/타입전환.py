import pandas as pd
import numpy as np

data = pd.read_csv('../data/auto-mpg.csv')
print(data.info())
print(data.head())

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)
print(data.head())

# 중복 배제하고 보여준다.
print( data['disp'].unique())

# 잘못된 데이터를 NaN으로 먼저 바꾼다.
# 정규식 sup 함수
data['disp'].replace('?', np.nan, inplace=True)
print(data.head())

data.dropna(subset=['disp'], axis=0, inplace=True)
print(data.head())
print(data.dtypes)
data['disp'] = data['disp'].astype('float')
print(data.dtypes)

# 범주형으로 바꾼다.
data['model'] = data['model'].astype('category')
print(data.dtypes)

# DataFrame의 버그(카테고리) - 그 범위를 벗어나는 데이터는 받으면 안 된다.
# 카테고리 타입에 데이터 추가했더니 스스로 float로 바뀐다.
# 허용되면 안 된다.
# 판다스 2.0에서 지원안함
# data = data.append({'mpg':90, 'model':93}, ignore_index=True)
# 판다스 2.0부터
data.loc[len(data)] = {'mpg':90, 'model':93}
# 모델 타입이 카테고리라서 없는 카테고리 값을 추가할 경우에 오류가 발생한다.
# 파일을 읽을 때 범위가 결정되어서 93이 해당사항이 없어서 에러가 발생한다.

# 반드시 범주형으로 되어야 할 것들은 범주형으로 바꿔줘야 한다.
print(data.dtypes)
print(data['model'].value_counts())     # 빈도표, 범주형의 경우에는 엄청 중요하다.

