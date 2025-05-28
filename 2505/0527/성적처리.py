from DBModule import Database
import sys
import os
# execptionUtil.py가 있는 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from execptionUtil import excUtil
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
class DBEngine:
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:1234@localhost/mydb",
            pool_size=10,       # 최대 연결 수
            max_overflow=5,     # 초과 시 추가 연결 수
            pool_recycle=3600   # 재활용 시간
        )

        try:
            self.conn = self.engine.connect()
            print("데이터베이스 연결 성공")
        except SQLAlchemyError as e:
            print("데이터베이스 연결 실패:", e)

    def output(self, sql):
        result = self.conn.execute(text(sql))
 
        rows = result.mappings().all()
        for row in rows:
            print(dict(row))

    def append(self):
        # 데이터추가하기 - 파라미터 처리방식
        sql = text("""
                insert into emp(empno, ename, sal)
                values(:empno, :ename, :sal)
            """)
        self.conn.execute(sql, [{"empno":10001, "ename": "우즈2", "sal": 8000},
                        {"empno":10002, "ename": "우즈3", "sal": 8000}])

        self.conn.commit()

    def close(self):
        self.conn.close()



class ScoreData:
    def __init__(self, sname="", kor=0, eng=0, mat=0, total=0, average=0):
        self.sname = sname
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.total = total
        self.average = average
            
    def output(self):
        print(self.sname, self.kor, self.eng, self.mat, self.total, self.average)

class ScoreManager:
    def output(self):
        sql = """
            select sname, kor, eng, mat
            , (kor+eng+mat) as total
            , (kor+eng+mat)/3 as average 
            from tb_score
        """
        db = Database()     # 객체 만들면 이미 디비 접근
        rows = db.executeAll(sql)
        self.dataList = []
        for row in rows:
            sname = row["sname"]
            kor = row["kor"]
            eng = row["eng"]
            mat = row["mat"]
            total = row["total"]
            avg = row["average"]
            s = ScoreData(sname, kor, eng, mat, total, avg)
            self.dataList.append(s)

        for s in self.dataList:
            s.output()
        db.close()

    # 추가
    def append(self):
        s = ScoreData()
        s.sname = input("이름 : ")
        s.kor = excUtil.getInt(str="국어 : ")
        s.eng = excUtil.getInt(str="영어 : ")
        s.mat = excUtil.getInt(str="수학 : ")

        sql = """
            insert into tb_score(sname, kor, eng, mat, regdate)
            values(%s, %s, %s, %s, now())
        """
        db = Database()     # 객체 만들면 이미 디비 접근
        db.execute(sql, (s.sname, s.kor, s.eng, s.mat))
        db.close()

    def update(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass

    def showMenu(self):
        print("*" * 12)
        print("1.전체 보기")
        print("2.추가")
        print("3.수정")
        print("4.삭제")
        print("5.검색")
        print("0.프로그램 종료")
        print("*" * 12)

    def close(self):
        pass

    def start(self):
        myFunc = [self.close, self.output, self.append, self.update, self.delete, self.search]
        while True:
            self.showMenu()
            str = "선택 >>"
            sel = excUtil.getInt(str=str, round=len(myFunc)-1)

            myFunc[sel]()

            if sel == 0:
                return

if __name__ == "__main__":
    sm = ScoreManager()
    sm.output()
    sm.start()

