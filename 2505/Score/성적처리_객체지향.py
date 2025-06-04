# 성적처리
# 이름,국어,영어,수학
# 총점, 평균, 학점

class Student:
    def __init__(self):
        self.name = ""
        self.kor = 0
        self.eng = 0
        self.mat = 0
        self.total = 0
        self.avg = 0
        self.grade = 0

    def isInt(self, n):
        for i in n:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                return False
    
    def inputScore(self, subject, round):
        while True:
            score = input(subject)
            if self.isInt(score) == False:
                print("양의 정수를 입력하세요.")
                continue
            score = int(score)
            if score < 0 or score > round:
                print(f"범위는 0~{round}입니다.")
                continue
            break

        return score
    
    def input(self):
        self.name = input("이름 >>")
        self.kor = self.inputScore("국어 >>", 100)
        self.eng = self.inputScore("영어 >>", 100)
        self.mat = self.inputScore("수학 >>", 100)

    def calcul(self):
        self.total = self.kor + self.eng + self.mat
        self.avg = self.total / 3
        
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
    
    def output(self):
        print(f"- {self.name} 학생 -")
        print(f"국어: {self.kor}, \t영어: {self.eng}, \t수학: {self.mat}")
        print(f"총점: {self.total}, \t평균: {self.avg:.2f}, \t점수: {self.grade}")

    def start(self):
        self.input()
        self.calcul()
        self.output()

class StudentManager:
    def __init__(self):
        self.studentList = []

    def isInt(self, n):
        for i in n:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                return False
    
    def inputStudents(self):
        while True:
            s = Student()
            s.start()
            self.studentList.append(s)
            n = input("그만 입력하고 싶으시면 0을 입력하세요. >>")
            if n == "0":
                break

    def ouputStudents(self):
        for s in self.studentList:
            s.output()

    def modifyStudent(self):
        studentIndex = []
        name = input("수정할 학생의 이름을 입력하세요. >>")
        for i, s in enumerate(self.studentList):
            if s.name == name:
                studentIndex.append(i)
        
        for i in range(len(studentIndex)):
            print(f"--- {i}번째 학생입니다. ---")
            s.output()
        
        sel = 0
        while True:
            sel = input("몇 번째 학생의 정보를 수정하고 싶으십니까? >>")
            if self.isInt(sel) == False:
                print("양의 정수를 입력하세요.")
                continue
            sel = int(sel)
            if sel < 0 or sel > len(studentIndex):
                print("범위 내의 수를 입력하세요.")
                continue
            break
        
        student = self.studentList[studentIndex[sel]]
        pass

    
    def initList(self):
        self.studentList.clear()

    def menuDisplay(self):
        print("1.학생 입력")
        print("2.학생들 정보 출력")
        print("3.학생 정보 수정")
        print("9.모두 초기화")
        print("0.종료")

    def start(self):
        while True:
            print()
            self.menuDisplay()
            sel = input("입력 >>")

            if sel == "1":
                self.inputStudents()
            elif sel == "2":
                self.ouputStudents()
            elif sel == "3":
                self.modifyStudent()
            elif sel == "9":
                self.initList()
            elif sel == "0":
                print("프로그램을 종료합니다.")
                return
            else:
                print("잘못 입력하셨습니다.")

if __name__ == "__main__":
    s = StudentManager()
    s.start()