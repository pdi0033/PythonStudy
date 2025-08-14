from fastapi import FastAPI 
from fastapi.responses import JSONResponse 

from fastapi import APIRouter, Depends 
from database import Database

from typing import Optional     
from fastapi import UploadFile, File, Form, HTTPException

# 파일 업로드 Depends   main.py파일과 board.py 간에 변수를 주고 받아야할 때 사용할 라이브러리

settings_container = {}
def get_settings():
    return settings_container.get("setting")


router = APIRouter(
    prefix="/board",  #url요청이 /board/~~~~ 로 오는것은 여기서 다 처리한다는 의미임 
    tags=["board"],     #swager문에 표시될 태그임   
    responses= {404:{'decription':'Not found'}} #예외처리 
)

@router.get("/")
def board_index():
    return {"msg":"접속성공"}

# 디비 데이터 들고오기
@router.get("/list")
def board_list():
    sql = """
    select id, title, writer, date_format(wdate, '%Y-%m-%d') wdate, 
    hit, filename, image_url
    from tb_board
    """

    print(sql)
    with Database() as db_mgr:
        results = db_mgr.executeAll(sql)
    return {"data":results}

# 데이터 추가 - 파일 업로드 받을 때는 multipart라는 방식으로 온다.
# Body, Pydemic 안 된다. Form으로만 받는다.
@router.post("/insert")
def board_insert(
    filename:Optional[UploadFile] = File(None),
    title:str = Form(...),      # Form 객체를 통해서 정보를 받는다. ...는 필수 필드
    writer:str = Form(...),
    contents:str = Form(...),
    settings:dict = Depends(get_settings)
):
    pass