# 여기는 관리하는 곳?으로 하자
from Board import Board
from Member import Member
from exceptionUtil import excUtil
from datetime import date
import pickle

class main:
    def __init__(self):
        self.mem = None
        self.memberList = []
        # self.memberList.append(Member())
        # self.saveMembers()
        self.readMembers()

        self.board = None
        self.boardList = []
        # self.boardList.append(Board())
        # self.saveBoards()
        self.readBoards()

        self.memInfoList = []
        for mem in self.memberList:
            self.memInfoList.append(mem.info)

    def saveMembers(self):
        with open("members.bin", "wb") as f:
            pickle.dump(self.memberList, f)

    def readMembers(self):
        self.memberList = excUtil.getListFromFile("members.bin")
        if self.memberList == []:
            self.memberList.append(Member())
            self.saveMembers()

    def saveBoards(self):
        with open("boards.bin", "wb") as f:
            pickle.dump(self.boardList, f)

    def readBoards(self):
        self.boardList = excUtil.getListFromFile("boards.bin")
        if self.boardList == []:
            self.boardList.append(Board())
            self.saveBoards()

    def getMem(self, id, pw):
        for mem in self.memberList:
            if id == mem.info["id"] and pw == mem.info["pw"]:
                return mem
        return -1
        
    def login(self):
        i = 1
        while i <= 3:
            id = input("ID >>")
            pw = input("PW >>")

            mem = self.getMem(id, pw)
            if mem == -1:
                print(f"{i}번 틀렸습니다.")
            else:
                print("로그인 성공")
                self.mem = mem
                return True
            i += 1
        print("로그인 실패")
        return False

    def boardDisplay(self):
        while True:
            for i, board in enumerate(self.boardList):
                print(f"[{i+1}]  [제목: {board.info["title"]}, 회원번호: {board.info["mNum"]}, 조회수: {board.info["view"]}]")
            print("[0]  나가기")
            
            str = "몇 번째의 게시글을 읽겠습니까? >>"
            sel = excUtil.getInt(round=(len(self.boardList)), str=str)
            if sel == 0:
                return
            
            isDelete = False
            if self.mem != None:
                isDelete = self.boardList[sel-1].start(self.mem.info["mNum"])
            else:
                isDelete = self.boardList[sel-1].start()

            if isDelete == 3:      #delete함
                self.boardList.pop(sel-1)
                self.saveBoards()
            

    def memManage(self):
        if self.mem == None:
            print("먼저 로그인 하셔야 합니다.")
            isLogin = self.login()
            if isLogin == False:
                return False
            
        isDelete = self.mem.start(self.memInfoList)
        if isDelete == 3:      #delete함
            # 그 회원이 쓴 모든 게시글 또한 삭제함.
            mNum = self.mem.info["mNum"]
            resultList = list(filter(lambda x: x.info["mNum"] == mNum, self.boardList))
            for board in resultList:
                self.boardList.remove(board)
            self.memberList.remove(self.mem)
            self.saveMembers()
            self.mem = None

    def writeBoard(self):
        if self.mem == None:
            print("먼저 로그인 하셔야 합니다.")
            isLogin = self.login()
            if isLogin == False:
                return False
        
        board = Board()
        board.setTitle()
        board.setDetail()
        board.setMemNum(self.mem.info["mNum"])
        board.setWriteNum(self.getNewWriteNum())
        board.updateDate()
        self.boardList.append(board)
        self.saveBoards()
    
    def getNewWriteNum(self):
        wNumList = []
        for board in self.boardList:
            wNumList.append(board.info["wNum"])
        newNum = int(max(wNumList)[1:]) + 1
        newNum = f"w{newNum:04d}"
        return newNum

    def newMem(self):
        #id, pw, name, phone, email
        member = Member(memInfoList=self.memInfoList)
        member.setId()
        member.setPw()
        member.setName()
        member.setPhone()
        member.setEmail()
        member.setMemNum(self.getNewMemNum())
        self.memberList.append(member)
        self.saveMembers()

    def getNewMemNum(self):
        mNumList = []
        for member in self.memberList:
            mNumList.append(member.info["mNum"])
        newNum = int(max(mNumList)) + 1
        newNum = f"{newNum:04d}"
        return newNum

    def menuDisplay(self):
        print("-" * 17)
        print(" " * 3, "게시판", " " * 3)
        print("-" * 17)
        print("[0]  떠나기")
        print("[1]  로그인")
        print("[2]  게시판 목록")
        print("[3]  게시글 작성")
        print("[4]  마이페이지")
        print("[5]  회원가입")

    def close(self):
        self.saveMembers()
        self.saveBoards()

    def start(self):
        while True:
            self.getNewWriteNum()
            funcList = [self.close, self.login, self.boardDisplay, self.writeBoard, self.memManage, self.newMem]
            self.menuDisplay()
            str = "선택 >>"
            sel = excUtil.getInt(round=(len(funcList)-1), str=str)

            sel = int(sel)
            funcList[sel]()
            if sel == 0:
                return

if __name__ == "__main__":
    m = main()
    m.start()