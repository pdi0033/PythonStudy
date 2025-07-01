import pandas as pd

data = {
    "name": ["홍길동", "임꺽정", "장길산", "홍경래"],
    "kor": [90, 80, 70, 70],
    "eng": [99, 98, 97, 46],
    "mat": [90, 70, 70, 60],
}

df = pd.DataFrame(data)
print(type(df))
print(df)

print(df.head(3))
print(df.iloc[0,0])
print(df.loc[0,"name"])

# 한 컬럼을 통으로
print(df['name'])
print(df['kor'])

print(df.columns)
for i in range(0,len(df)):
    print(df.iloc[i, 0])

for i in range(0,df.shape[0]):
    for j in range(0, df.shape[1]):
        print(df.iloc[i, j], end=' ')
    print()

print("="*20)

print(df.iloc[2:4, 2])
print(df.iloc[2:4, 2:4])
print(df.loc[0, 'name'])
print(df.loc[3, 'eng'])
print(df.loc[:, 'name':'eng'])

