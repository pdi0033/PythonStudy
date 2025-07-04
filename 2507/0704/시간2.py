import datetime
import calendar

start_day, end_day = calendar.monthrange(2025, 7)
print(start_day, end_day)

for i in range(1, 13):
    start_day, end_day = calendar.monthrange(2025, i)
    print(f"{i}달의 마지막 날은 {end_day} 입니다.")


import pandas as pd
import numpy as np

date_str = ["2019-10-01", "2019-10-02", "2019-10-03", "2019-10-04"]
idx = pd.to_datetime(date_str, infer_datetime_format=True)
print(type(idx))
print(idx)

np.random.seed(0)
s = pd.Series(np.random.randn(4), index=idx)
print(s)

#인덱스를 이용하여 출력할 수 있다 
print(s['2019-10-01'])
print(s['2019-10-02'])




