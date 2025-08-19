# 파일처리와 관련된 모듈 import
import os, shutil
from typing import Optional     
# 최근에 언어들 경향이 null이나 None값에 대한 처리를 철저하게 하기 위해 만든 라이브러리 Optional(객체) 
# 이 객체는 할당이 안 되었을 수도 있다는 의미
from fastapi import UploadFile, File, Form, HTTPException
"""
get 방식 - 2048 byte 미만의 텍스트
post 방식 - url-encoding방식, FormData 방식(파일 업로드), raw(json)
            특별히 요청을 안 하면 raw(json), 파일 업로드처리를 하려면 Form 객체를 통해서 데이터를 수신해야만 한다.

이미지를 업로드하고 나면 업로드 경로를
http://127.0.0.1:8000/image_url/파일명
물리적 경로를 url로 바꾸는 방법이 필요하다.
"""
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi import Body
# CORSMiddleware
# 나하고 도메인 또는 아이피와 포트번호가 다른 애들은 (브라우저 제외) 자바스크립트로 남의 사이트 접근 거부가 원칙
# 근데 가끔은 예외가 필요하다.
# 그 예외를 처리하는 미들웨어이다.

# FastAPI 애플리케이션 초기화
app = FastAPI()     # 객체를 만들면 웹서버 만들어짐

# 모든 라우터가 공유해야할 변수가 있을 때
my_global_settings = {
    "api_key":"1203ue",
    "db_url":"",
    "UPLOAD_DIRECTORY":"./upload_files"
}

# 1. 업로드 디렉토리가 없을 경우에 디렉토리를 만들자.
if not os.path.exists(my_global_settings["UPLOAD_DIRECTORY"]):
    os.makedirs(my_global_settings["UPLOAD_DIRECTORY"])

# 2. ./upload_files => url로 바꾸는 작업이 필요하다.
# 정적
app.mount("/static", 
          StaticFiles(directory=my_global_settings["UPLOAD_DIRECTORY"]), 
          name="static")


# 미들웨어 - 중간에 거쳐간다. 클라이언트 ====> 미들웨어1 => 미들웨어2 => 미들웨어3 ... ====> 서버

# CORS(Cross-Origin Resource Sharing) 설정
# 풀스택개발 - 프론트앤드(사용자인터페이스, 눈에 보이는 부분만 담당, html, css, javascript-react 등)
            # 백앤드 - Restful API 서버 - 데이터를 보통 json형태로 응답해주는 서버이다.
            # fastapi, 장고, 플라스크, 스프링, php, nodejs 등 ...
            # 백앤드와 프론트앤드는 별도의 서버이다.
            # 서로 간에 자바스크립트를 통해 데이터를 주고 받아야 하는데 서로 다른 사이트이다.
            # CORS(왜 남의 사이트에서 내 사이트를 오는데?라는 오류임)
            # 백앤드에서 이 문제를 해결해줘야 한다. 
            # 특정 아이피나 도메인 그리고 포트번호는 내 정보를 가져갈 수 있어라고 허락이 필요하다.
            # CORSMiddleware를 통해서 이걸 열어준다.
            # 프론트쪽에 프록시 서버를 만들어서 접근 가능하다. => react는 아예 허용 안함, vuejs는 아직 허용중이긴 한데 고려하지 말자.
            # 쓰면 안 된다. 보안이 취약해짐.
# React 개발 서버(localhost:3000 등)와 통신하기 위해 필요합니다.
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://www.sessac.com:5173"
]

app.add_middleware(     # 필요한 미들웨어를 추가시킨다.
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# @-데코레이터 app
@app.get("/")
def index():
    return {"message":"Hello FastAPI"}

# 라우터 연결하기
from routers import board, mnist, predict

# 모듈과 모듈 간에 전역 변수는 원칙적으로 없다.
# 전달
# Dependency Injection - 의존성 강제주입
board.settings_container["settings"] = my_global_settings
predict.settings_container["settings"] = my_global_settings

app.include_router(board.router)        # http://127.0.0.1:8000/board ~~ ==> board.py가 처리한다.
app.include_router(mnist.router)
app.include_router(predict.router)

# 실행방법
# conda activate backend
# backend 폴더까지 가기
# python -m uvicorn main:app --reload --port 8000

# 확인
# 브라우저: 127.0.0.1:8000
# 스웨거: 127.0.0.1:8000/docs

# cmd
# conda install pymysql sqlalchemy
# conda install python-multipart    # 파일 업로드 라이브러리
