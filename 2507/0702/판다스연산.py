import pandas as pd

data1 = {'kor':90, 'mat':80}
data2 = {'eng':80, 'mat':70, 'kor':90}
data3 = {'kor':90, 'mat':70, 'eng':80}
data4 = {'kor':90, 'eng':80}           

# 키가 없으면 NaN으로 받아들인다. NaN에 연산이 불가함.
s1 = pd.Series(data1)
s2 = pd.Series(data2)
s3 = pd.Series(data3)
s4 = pd.Series(data4)

result = s1 + s2 + s3 + s4
result2 = result / 4

print(result)
print(result2)

result3 = s1.add(s2, fill_value=0).add(s3, fill_value=0).add(s4, fill_value=0)
print(result3)



