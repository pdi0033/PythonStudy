# 회원관리 - 회원번호, 회원아이디, 패스워드, 이름, 전화번호, 이메일
# 게시판 - 회원번호, 글번호, 제목, 내용, 작성일, 조회수

# 회원가입 수정, 탈퇴, 조회(자기정보)
# 게시글 작성 - 회원번호, 제목, 내용, 작성일(date 라이브러리 사용),
#               조회수 0, 읽어보기, 수정(글쓴이만) 회원번호랑 패스워드 입력하면, 삭제(글쓴이만)

import pickle
from datetime import date
from exceptionUtil import excUtil

class Board:
    info = {}
    def __init__(self, mNum="0001", wNum="w0001", title="ImMember", detail="none", date="2000-01-01", view=0):
        if self.info == {}:
            self.info = {
                "mNum": mNum,
                "wNum": wNum,
                "title": title,
                "detail": detail,
                "date": date,
                "view": view
            }

        self.canModify = False

    def setTitle(self):
        title = ""
        while title == "":
            title = input("제목 >>")
        self.info["title"] = title

    def setDetail(self):
        detail = ""
        while detail == "":
            detail = input("내용 >>")
        self.info["detail"] = detail

    def setMemNum(self, s):
        self.info["mNum"] = s

    def setWriteNum(self, s):
        self.info["wNum"] = s
        
    def readAll(self):
        print("-" * 17)
        print(" " * 3, f"회원번호: {self.info["mNum"]}, 제목: {self.info["title"]}, 조회수: {self.info["view"]}", " " * 3)
        print("-" * 17)
        print(f"글번호: {self.info["wNum"]}")
        print(f"작성일: {self.info["date"]}")
        print(f"내용: {self.info["detail"]}")
        self.info["view"] += 1
    
    def close(self):
        pass

    def updateDate(self):
        today = date.today()
        self.info["date"] = today

    def modify(self):
        modifyList = [self.close, self.setTitle, self.setDetail]
        while True:
            self.readAll()
            print("* 제목과 내용만 수정하실 수 있습니다. 수정하면 자동으로 작성일이 업데이트 됩니다.")
            print("[1]  제목")
            print("[2]  내용")
            print("[0]  떠나기")
            str = "어느 정보를 수정하고 싶으십니까?"
            sel = excUtil.getInt(round=len(modifyList), str=str)

            sel = int(sel)
            modifyList[sel]()
            if sel == 0:
                return
            
            self.updateDate()
        

    def delete(self):
        print("삭제했습니다.")

    def menuDisplay(self):
        print("[0]  떠나기")
        #print("[1]  읽어보기")
        if self.canModify == True:
            print("[1]  수정")
            print("[2]  삭제")

    def start(self, mNum=""):
        if self.info["mNum"] == mNum:
            self.canModify = True
        else:
            self.canModify = False
        while True:
            funcList = [self.close, self.modify, self.delete]
            self.readAll()
            self.menuDisplay()
            str = "선택 >>"
            if self.canModify == True:
                sel = excUtil.getInt(round=(len(funcList)-1), str=str)
            else:
                sel = excUtil.getInt(round=0, str=str)

            sel = int(sel)
            funcList[sel]()
            if sel == 0:
                return
            elif sel == 2:
                self.close()
                return 3

if __name__ == "__main__":
    b = Board(wNum="w0001")
    # boardList = []
    # boardList.append(b)
    # with open("boards.bin", "wb") as f:
    #     pickle.dump(boardList, f)
    b.start()