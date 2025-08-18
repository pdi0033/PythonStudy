from fastapi import FastAPI 
from fastapi.responses import JSONResponse 

from fastapi import APIRouter, Depends 
from database import Database

import os, shutil, io
from typing import Optional     
from fastapi import UploadFile, File, Form, HTTPException

import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# 파일 업로드 Depends   main.py파일과 board.py 간에 변수를 주고 받아야할 때 사용할 라이브러리

settings_container = {}
def get_settings():
    return settings_container.get("settings")


router = APIRouter(
    prefix="/mnist",  #url요청이 /board/~~~~ 로 오는것은 여기서 다 처리한다는 의미임 
    tags=["mnist"],     #swager문에 표시될 태그임   
    responses= {404:{'decription':'Not found'}} #예외처리 
)

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
    
# 모델 로드
model = ImageClassifier()
model.load_state_dict(torch.load("../../../pytorch/0818/mnist_model.pth", map_location="cpu"))
model.eval()

# 훈련할 때 썼던 transform 그대로 사용
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

@router.get("/")
def mnist_index():
    return {"msg":"접속성공"}

# 데이터 추가 - 파일 업로드 받을 때는 multipart라는 방식으로 온다.
# Body, Pydemic 안 된다. Form으로만 받는다.
# 4️⃣ 예측 엔드포인트
@router.post("/predict")
async def mnist_predict(file: UploadFile = File(...)):
    # 파일을 이미지로 변환
    img = Image.open(file.file).convert("L")  # 흑백
    img = transform(img).unsqueeze(0)         # 배치 차원 추가 (1, 1, 28, 28)

    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)
        predicted_class = predicted.item()

    return {"filename": file.filename, "predicted": predicted_class}