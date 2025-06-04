# 회원관리 - 회원번호, 회원아이디, 패스워드, 이름, 전화번호, 이메일
# 게시판 - 회원번호, 글번호, 제목, 내용, 작성일, 조회수

# 회원가입 수정, 탈퇴, 조회(자기정보)
# 게시글 작성 - 회원번호, 제목, 내용, 작성일(date 라이브러리 사용),
#               조회수 0, 읽어보기, 수정(글쓴이만) 회원번호랑 패스워드 입력하면, 삭제(글쓴이만)

import pickle
import re
from exceptionUtil import excUtil

class Member:
    info = {}
    def __init__(self, mNum="0001", id="member01", pw="1234", name="ImMember", phone="010-0000-0001", email="mem01@sesac.com",
                 memInfoList = []):
        if self.info == {}:
            self.info = {
                "mNum": mNum,
                "id": id,
                "pw": pw,
                "name": name,
                "phone": phone,
                "email": email
            }
        
        self.memInfoList = memInfoList
        self.isOut = False


    def getNoDup(self, str="", key="mNum", alphaNum=False):
        while True:
            info = input(f"{str} >>")
            if alphaNum == True:
                if excUtil.isAlphaNum(info) == False:
                    continue

            for mem in self.memInfoList:
                if info == mem[key]:
                    print(f"이미 있는 {str}입니다.")
                    continue
            return info
    
    def setMemNum(self, mNum=""):
        self.info["mNum"] = mNum
    
    def setId(self):
        str = "ID"
        self.info["id"] = self.getNoDup(str=str, key="id", alphaNum=True)
    
    def setPw(self):
        pw = ""
        while True:
            pw = input("PW >>")
            if excUtil.isAlphaNum(pw) == False:
                continue
            break
        self.info["pw"] = pw
    
    def setName(self):
        name = ""
        while name == "":
            name = input("이름 >>")
        self.info["name"] = name

    def setPhone(self):
        # 전화번호 체크 패턴       r"\d{3}-\d{4}-\d{4}“
        phonePattern = r"\d{2,3}-\d{3,4}-\d{3,4}"
        regex = re.compile(phonePattern)

        phone = ""
        while True:
            phone = input("전화번호 >>")
            result = regex.match(phone)
            if result != None:
                break
            else:
                print("000-0000-0000처럼 휴대전화나 집 전화번호를 써주세요.")
        self.info["phone"] = phone
        

    def setEmail(self):
        # 이메일 체크 패턴 r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b"
        emailPattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$"
        regex = re.compile(emailPattern)

        email = ""
        while True:
            email = input("이메일 >>")
            result = regex.match(email)
            if result != None:
                break
            else:
                print("xxxx@email.com처럼 형식을 지켜 써주세요.")
        self.info["email"] = email
        
    
    def check(self):
        print("-" * 17)
        print(f"     회원번호: {self.info["mNum"]}")
        print(f"[1]  ID: {self.info["id"]}")
        print(f"[2]  PW: {self.info["pw"]}")
        print(f"[3]  이름: {self.info["name"]}")
        print(f"[4]  전화번호: {self.info["phone"]}")
        print(f"[5]  이메일: {self.info["email"]}")

    
    def modify(self):
        modifyList = [self.close, self.setId, self.setPw, self.setName, self.setPhone, self.setEmail]
        while True:
            self.check()
            print("[0]  떠나기")
            print("* 회원번호는 수정할 수 없습니다.")
            str = "어느 정보를 수정하고 싶으십니까?"
            sel = excUtil.getInt(round=len(modifyList), str=str)

            sel = int(sel)
            modifyList[sel]()
            if sel == 0:
                return

    def secession(self):
        pw = input("탈퇴하시려면 PW를 입력해주세요. >>")
        if pw == self.info["pw"]:
            print("탈퇴하셨습니다.")
            self.isOut = True
        else:
            print("잘못 작성하셨습니다.")
            self.isOut = False

    def menuDisplay(self):
        print("-" * 17)
        print(" " * 3, "회원 관리", " " * 3)
        print("-" * 17)
        print("[0]  떠나기")
        print("[1]  내 정보 조회")
        print("[2]  내 정보 수정")
        print("[3]  탈퇴하기")
    
    def close(self):
        pass

    def start(self, memInfoList):
        self.memInfoList = memInfoList
        while True:
            funcList = [self.close, self.check, self.modify, self.secession]
            self.menuDisplay()
            str = "선택 >>"
            sel = excUtil.getInt(round=(len(funcList)-1), str=str)

            sel = int(sel)
            funcList[sel]()
            if sel == 0:
                return
            
            if sel == 3:
                if self.isOut == True:
                    return 3
            

if __name__ == "__main__" :
    m = Member(id="member01", pw="1234")
    # memList = []
    # memList.append(m)
    # with open("members.bin", "wb") as f:
    #     pickle.dump(memList, f)
    m.start()