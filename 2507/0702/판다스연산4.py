import pandas as pd
data = {
    'x1':[2.9, 2.4, 2, 2.3, 3.2],
    'x2':[9.2, 8.7, 7.2, 8.5, 9.6],
    'x3':[13.2, 11.5, 10.8, 12.3, 12.6],
    'x4':[2, 3, 4, 2, 3]
}
df = pd.DataFrame(data)

data1 = {'x1':10, 'x2':20, 'x3':30, 'x4':40}
df.loc[len(df)] = data1
print(df)

df['total'] = df['x1'] + df['x2'] + df['x3'] + df['x4']
print(df)

