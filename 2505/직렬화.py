import pickle
data = {"name": "홍길동", "age": 23, "phone": ["010-0000-0001", "010-0000-0002"]}

#직렬화
with open("data.bin", "wb") as f:
    pickle.dump(data, f)

#역직렬화
with open("data.bin", "rb") as f:
    data2 = pickle.load(f)
    
print(type(data2), data2)