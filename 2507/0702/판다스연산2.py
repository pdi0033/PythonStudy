import pandas as pd

data1 = {'kor':90, 'mat':80, 'eng':90}
data2 = {'eng':80, 'mat':70, 'kor':90}
data3 = {'kor':90, 'mat':70, 'eng':80}
data4 = {'kor':90, 'eng':80, 'mat':100}           

df = pd.DataFrame()
# pandas 2.0 이후에 append 함수가 없어졌다.
# df = df.append(data1, ignore_index=True)

df = pd.DataFrame(columns=['kor', 'eng', 'mat'])
df.loc[len(df)] = data1     # 이렇게 바뀌었음
df.loc[len(df)] = data2
df.loc[len(df)] = data3
df.loc[len(df)] = data4
print(df)

# 여러 개의 데이터 프레임을 합칠 수도 있다. concat
df = pd.concat([
    pd.DataFrame([data1]),
    pd.DataFrame([data2]),
    pd.DataFrame([data3]),
    pd.DataFrame([data4]),
], ignore_index=True)
print("\nconcat 결과:")
print(df)

df['total'] = df['kor'] + df['eng'] + df['mat']
df['avg'] = df['total'] // 3
print(df)


