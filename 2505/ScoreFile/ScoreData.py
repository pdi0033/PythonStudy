class ScoreData:
    def __init__(self, name="", kor = 0, eng = 0, mat = 0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = self.kor + self.eng + self.mat
        self.avg = self.total / 3
        self.getGrade()

    def getGrade(self):
        if self.avg >= 90:
            self.grade = "수"
        elif self.avg >= 80:
            self.grade = "우"
        elif self.avg >= 70:
            self.grade = "미"
        elif self.avg >= 60:
            self.grade = "양"
        else:
            self.grade = "가"

        return self.grade

    def output(self):
        print(f"이름: {self.name}", end='\t')
        print(f"국어: {self.kor}", end='\t')
        print(f"영어: {self.eng}", end='\t')
        print(f"수학: {self.mat}", end='\t')
        print(f"총합: {self.total}", end='\t')
        print(f"평균: {self.avg:.2f}", end='\t')
        print(f"학점: {self.grade}", end='\n')


if __name__ == "__main__":
    f = open("score.txt", "r", encoding='utf-8')
    txtList = f.readlines()
    f.close()

    scoreList = []

    # \n삭제
    for st in txtList:
        if '\n' in st:
            st = st[:len(st)-1]
    
    for st in txtList:
        name, kor, eng, mat = st.split(',')
        kor = int(kor)
        eng = int(eng)
        mat = int(mat)
        s = ScoreData(name, kor, eng, mat)
        scoreList.append(s)

    for s in scoreList:
        s.output()
