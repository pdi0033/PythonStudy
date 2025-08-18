import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from sklearn.datasets import fetch_california_housing   # fetch - 데이터가 양이 많아서 다운로드 받기
import pandas as pd

df = pd.read_csv("../../data/diamonds.csv")
print(df.head())
print(df.info())
print(df.describe())
# ["carat","cut","color","clarity","depth","table","price","x","y","z"]
# df.drop('color', axis=1, inplace=True)

# 1. 결측치
df = df.dropna(how='any', axis=0)
print(df.isnull().sum())

# 원핫 인코딩
X = df.iloc[:, [0,1,3,4,5,7,8,9]]   # color 무시
y = df.loc[:, 'price']    # mpg
X = pd.get_dummies(X)
print(X.head())
print(X.shape)

# 3. 스케일링
# 데이터 표준화
scaler = StandardScaler()
X = scaler.fit_transform(X)
le = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.to_numpy(), dtype=torch.float32).view(-1, 1)     # 회귀나 2진분류일 경우 1차원임 => 2차원
# y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)     # 회귀나 2진분류일 경우 1차원임 => 2차원

X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.to_numpy(), dtype=torch.float32).view(-1, 1)
# y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

class HousingClassifier(nn.Module):
    def __init__(self):
        super(HousingClassifier, self).__init__()
        self.input = nn.Linear(19, 64)    # 특성 19
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, 32)
        self.output = nn.Linear(32, 1)     # 결과값이 하나임

    def forward(self, x):
        x = self.input(x)
        x = self.relu(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.output(x)
        
        return x

model = HousingClassifier()
criterion = nn.MSELoss()  # Mean Squared Error 평균제곱곱차
optimizer = optim.Adam(model.parameters(), lr=0.001)

def train_model(epochs):
    model.train()   # 학습모드
    for epoch in range(epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            optimizer.step()
        print(f'Epoch: {epoch+1}/{epochs}, Loss: {loss.item()}')
    print('학습완료')

# 평가는 다르게
def evaluate_model():
    model.eval()   # 평가모드
    with torch.no_grad():
        total_loss = 0
        total_samples = 0
        for inputs, labels in test_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            total_samples += inputs.size(0)
            total_loss += loss.item() * inputs.size(0)

        # MSE와 RMSE 계산
        avg_mse = total_loss / total_samples
        rmse = np.sqrt(avg_mse)
        
        print(f'테스트 데이터셋 평균 MSE: {avg_mse:.4f}')
        print(f'테스트 데이터셋 RMSE   : {rmse:.4f}')

if __name__ == "__main__":
    train_model(epochs=1000)
    evaluate_model()
    pass