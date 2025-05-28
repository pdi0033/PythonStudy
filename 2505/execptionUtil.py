# import sys
# import os
# # execptionUtil.py가 있는 상위 디렉토리를 sys.path에 추가
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from execptionUtil import excUtil

class excUtil:
    #예외처리는 끝이 없고......
    #나는 죽었다.......
    @classmethod
    def isInt(cls, s):
        try:
            int(s)
        except ValueError:
            return False
        return True

    @classmethod
    def getInt(cls, str="", round = 100, min = 0):
        while True:
            num = input(str)
            if cls.isInt(num) == False:
                print("정수를 입력해주세요.")
                continue
            num = int(num)

            # 범위가 아닐때
            if num < min or num > round:
                print(f"{min}이상 {round}이하로 입력해주세요.")
                continue

            return num
        
    @classmethod
    def isAlpha(cls, s):
        # 아무것도 입력 안 했을때
        if s == "":
            return False
        
        for i in s:
            if (ord(s) < ord('a') or ord(s) > ord('z')) and (ord(s) < ord('A') or ord(s) > ord('Z')):
                return False
        return True
    
    @classmethod
    def isAlphaNum(cls, s):
        for i in s:
            if cls.isAlpha(i) == False and cls.isInt(i) == False:
                print("정수와 알파벳만 사용하여 작성해 주세요.")
                return False
        return True
    
    @classmethod
    def getListFromFile(cls, fileName=""):
        try:
            with open(fileName, "rb") as f:
                getList = pickle.load(f)
                return getList
        except Exception as e:
            return []