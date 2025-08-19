# 1. mnist 학습한 내용을 모델로 저장
# 2. fastapi 서버 만들고, 프론트는 생략
    # 스웨거 => 이미지 업로드(0, 1 올리면) 입력한 데이터 맞추기

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import torchvision.datasets as datasets
import torchvision.transforms as transforms

# 1. 하이퍼파라미터 설정하기
batch_size = 64     # 메모리가 적어서 못 갖고 오면 이걸 줄이면 된고 메모리가 충분하면 값을 늘린다.
learning_rate = 0.001
epochs = 100
# 장치가 gpu가 있으면 gpu를 쓰고 없으면 cpu 쓰기
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 2. 데이터준비
# 이미지 전처리를 위한 변환 정의
transform = transforms.Compose([
    transforms.ToTensor(),      # PIL 이미지를 PyTorch 텐서로 변환한다. (0~1 사이의 값)
    transforms.Normalize( (0.5,), (0.5,) )  # 텐서를 평균 0.5, 표준편차 0.5로 정규화한다.
])

# 3. 데이터셋 다운로드 및 로드
train_dataset = datasets.MNIST(root="../../data", train=True, transform=transform, download=True)
train_loader = DataLoader(dataset= train_dataset, batch_size=batch_size, shuffle=True)

test_dataset = datasets.MNIST(root="../../data", train=False, transform=transform, download=True)
test_loader = DataLoader(dataset= test_dataset, batch_size=batch_size, shuffle=True)

# 4. 완전연결신경망 만들기
class ImageClassifier(nn.Module):
    def __init__(self, input_size=28*28, hidden_size=500, num_classes=10):
        # 그림 크기가 28 by 28
        super(ImageClassifier, self).__init__()     # 첫번째인자: 클래스명, 두번째인자: 객체자신
        self.fc1 = nn.Linear(input_size, hidden_size)    # 784 -> 500
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)  # 500 -> 10개로 

    def forward(self, x):
        # 이미지를 1차원 벡터로 만들어서 전달해야 한다.
        x = x.reshape(-1, 28*28)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 5. 모델 만들기
model = ImageClassifier()

# 6. 손실함수와 옵티마이저 정의하기
criterion = nn.CrossEntropyLoss()   # 손실함수 - 다중분류, softmax를 제공함.
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)     # 옵티마이저

def train_model(epochs=100):
    for epoch in range(epochs):
        for i, (images, labels) in enumerate(train_loader):
            # 순전파
            outputs = model(images)
            loss = criterion(outputs, labels)   # 손실계산
            optimizer.zero_grad()   # 가중치 초기화
            loss.backward()     # 역전파
            optimizer.step()     # 가중치 업데이트
            if (i+1)%100 == 0:
                print(f'Epochs [{epoch+1}/{epochs}]  Step [{i+1}/{len(train_loader)}]  Loss {loss.item():.4f}')
    
    save_model()

def evaluate_model():
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct/total
    print(f"테스트셋 정확도: {accuracy:.2f}")

def save_model():
    torch.save(model.state_dict(), "mnist_model.pth")   # 학습한 내용을 저장

# 이미지 하나를 읽어서 예측하기
# 이미지 처리 라이브러리
from PIL import Image
def predict_image(image_path):
    try:
        # 모델 구조를 다시 정의하고 가중치를 로드하거나, 전체 모델을 로드
        # 여기서는 전체 모델을 로드하는 방식으로 진행
        # 1. 모델 클래스 인스턴스 생성 (필수)
        loaded_model = ImageClassifier()    # fastapi쪽에 클래스가 있어야 한다.
        # 2.state_dict 로드
        loaded_model.load_state_dict(torch.load("mnist_model.pth"))
    except FileNotFoundError:
        print("Error: Thre trained model file 'mnist_model.pth' was not found.")
        exit()
    
    # 1. 이미지 불러오기
    try:
        image = Image.open(image_path).convert('L')     # 'L'모드로 변환하여 흑백 이미지로 만듦
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
        return None
    
    # 2. 이미지 전처리
    # 모델 학습 시 사용한 것과 동일한 전처리 과정을 적용
    transform = transforms.Compose([
        transforms.Resize((28,28)),             # 이미지를 28*28 크기로 조정
        transforms.ToTensor(),                  # PIL 이미지를 PyTorch 텐서로 변환(0~1)
        transforms.Normalize((0.5,), (0.5,))    # 텐서를 정규화
    ])

    # 전처리된 이미지를 텐서로 변환
    image_tensor = transform(image)

    # 3. 모델 입력 형태로 변경
    # DataLoader는 배치 차원을 자동으로 추가하지만, 여기서는 직접 추가해야 함
    image_tensor = image_tensor.unsqueeze(0)    # [1, 1, 28, 28]

    # 4. 모델로 예측
    # 모델을 추론 모드로 전환
    loaded_model.eval()
    with torch.no_grad():
        output = loaded_model(image_tensor)
        # Softmax를 적용하여 확률로 변환
        probabilities = torch.nn.functional.softmax(output, dim=1)
        # 가장 높은 확률을 가진 클래스(숫자)와 그 확률을 찾음
        _, predicted_class = torch.max(probabilities, 1)
        predicted_prob = probabilities[0][predicted_class].item()

        if predicted_prob is not None:
            print(f"이미지 '{image_path}'의 예측 결과: {predicted_class}")
            print(f"예측 확률: {predicted_prob:.4f}")

        return predicted_class, predicted_prob

if __name__ == "__main__":
    # train_model(epochs=10)
    # evaluate_model()

    # 예측하려는 JPEG 파일 경로를 입력
    image_path = '../../data/MNIST/mnist/2.jpg'

    # 예측
    predict_image(image_path)
