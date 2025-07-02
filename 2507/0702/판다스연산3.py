import pandas as pd
data = {
    'fruits':['망고', '딸기', '수박', '파인애플'],
    'price':[2500, 5000,10000, 7000],
    'count':[5, 2, 2, 4],
}
df = pd.DataFrame(data)

#새로운 행 추가하기 , 주의 : 반드시 반환되는 값을 받아야 추가가 된다 
#append 함수는 데이터가 추가된 객체를 반환한다 . 
# df.append({'fruits':'사과', 'price':3500, 'count':10} , ignore_index=True)
data1 = {'fruits':'사과', 'price':3500, 'count':10}
# df = pd.concat([
#     df,
#     pd.DataFrame([data1])
# ], ignore_index=True)
df.loc[len(df)] = data1   
print(df)

df2 = df.drop('price', axis=1)      # axis-축   0-행  1-열
print('원본')
print(df)
print('열 삭제')
print(df2)

df2 = df.drop(0, axis=0)
df2 = df2.reset_index()     # 인덱스를 다시 부여해라
print(df2)
