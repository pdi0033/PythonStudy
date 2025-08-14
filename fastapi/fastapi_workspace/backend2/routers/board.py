from fastapi import FastAPI 
from fastapi.responses import JSONResponse 

from fastapi import APIRouter, Depends 
from database import Database

import os, shutil
from typing import Optional     
from fastapi import UploadFile, File, Form, HTTPException

# 파일 업로드 Depends   main.py파일과 board.py 간에 변수를 주고 받아야할 때 사용할 라이브러리

settings_container = {}
def get_settings():
    return settings_container.get("settings")


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
    temp_filename=""
    temp_img_url=""


    # 파일 업로드 먼저 처리하기
    if filename and filename.filename:
        file_location = os.path.join(settings["UPLOAD_DIRECTORY"],
                                     filename.filename)
        # 클라이언트로부터 파일을 받아온다.
        # 이때 모든 정보는 filename 객체로 받아옴.
        # 이 객체는 filename 속성도 있고, file 정보 속성도 있다.
        # 확인해서 파일 정보가 맞지 않으면 정지시키거나 지나치게 용량이 커도 안 된다.
        # 용량 확인도 해줘야 하는데 copyfileobj를 통해서 서버 폴더에 저장함.
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(filename.file, buffer)

        temp_filename = filename.filename
        temp_img_url = "static/" + temp_filename

        file_response = f"파일 {filename.filename}가 업로드 되었습니다."
    else:
        file_response = "파일이 첨부되지 않았습니다."

    sql = """
        insert into tb_board (title, writer, contents, filename, image_url, wdate, hit)
        values (:title, :writer, :contents, :filename, :image_url, now(), 0)
    """

    with Database() as db_mgr:
        data = [{"title": title, "writer":writer, "contents":contents,
                 "filename":temp_filename, "image_url":temp_img_url}]
        db_mgr.execute(sql, data)
    
    return {"msg":"등록성공"}

# http://127.0.0.1:8000/static/5547758_eea9edfd54_n.jpg

@router.get("/view/{id}")
def board_view(id:int):
    sql = """
        select id, title, writer, date_format(wdate, '%Y-%m-%d') wdate, 
        hit, filename, image_url, contents
        from tb_board
        where id=:id
    """
    data = [{"id":id}]
    print(sql)
    with Database() as db_mgr:
        results = db_mgr.executeAll(sql, data)
    return {"data":results}