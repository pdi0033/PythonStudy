import pandas as pd
import numpy as np

data = pd.read_csv('../data/auto-mpg.csv')

print(data.head())
print(data.info())

# 컬럼명 변경하기 => 프로그램 안에서 바꾸기
data.columns = ['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.head())

# 정규화
# (정규화하고자하는값 - 최소값) / (최대값 - 최소값)
data['mpg2'] = (data['mpg'] - data['mpg'].min()) / (data['mpg'].max() - data['mpg'].min())

# 단위환산
mpg_unit = 1.60934 / 3.78541
data['kpl'] = (data['mpg']*mpg_unit).round(2)   # 소수점 2자리 반올림
print(data.head())

