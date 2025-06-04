from ScoreData import ScoreData

class ScoreManager:
    def __init__(self):
        self.scoreList = []
        self.readFile()

    def readFile(self):
        f = open("score.txt", "r", encoding="utf-8")
        txtList = f.readlines()
        f.close()

        for st in txtList:
            st = st.strip()

        for st in txtList:
            name, kor, eng, mat = st.split(',')
            kor = int(kor)
            eng = int(eng)
            mat = int(mat)
            s = ScoreData(name, kor, eng, mat)
            self.scoreList.append(s)
    
    def output(self):
        for s in self.scoreList:
            s.output()


if __name__ == "__main__":
    sm = ScoreManager()
    sm.output()
