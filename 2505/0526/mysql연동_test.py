# insert into tb_score(sname, kor, eng, mat, regdate)
# 	values('홍길동', 90,90,90,now());
# select id, sname, kor, eng, mat, (kor+eng+mat) as total, date_format(regdate, '%Y-%m-%d %H:%i:%s') from tb_score;

# -- 전체보기
# -- 추가: 입력받아서
# -- 수정
# -- update 테이블명 set 필드1='값1', 필드2='값2', ... where절
# -- 삭제
# -- delete from 테이블명 where id=1
# -- 검색
import pymysql
import pymysql.cursors


class SqlTest:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',    # ip localhost = 127.0.0.1
                       user='user02',         # 아이디
                       password='qwer1234',     # 패스워드
                       db='mydb',           # 데이터베이스명
                       port=3306) 
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def isInt(self, s):
        try:
            int(s)
        except ValueError:
            return False
        return True

    def getInt(self, str="", round = 100, min = 0):
        while True:
            num = input(str)
            if self.isInt(num) == False:
                print("정수를 입력해주세요.")
                continue
            num = int(num)

            # 범위가 아닐때
            if num < min or num > round:
                print(f"{min}이상 {round}이하로 입력해주세요.")
                continue

            return num
    def showAll(self):
        sql = """select id, sname, kor, eng, mat
        , (kor+eng+mat) as total
        , ((kor+eng+mat) / 3) as avg
        , date_format(regdate, '%Y-%m-%d %H:%i:%s') as date 
        from tb_score;"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("-" * 12)
        print("데이터개수", len(rows))
        for row in rows:
            print(f"id: {row['id']}, 이름: {row['sname']}, 국어: {row['kor']}, 영어: {row['eng']}, 수학: {row['mat']}, 총합: {row['total']}, 평균: {row['avg']:.2f}, 날짜: {row['date']}")
        
        return len(rows)
    
    def insert(self):
        sname = input("이름 >>")
        kor = self.getInt(str="국어 >>")
        eng = self.getInt(str="영어 >>")
        mat = self.getInt(str="수학 >>")

        sql = """
            insert into tb_score(sname, kor, eng, mat, regdate)
            values(%s, %s, %s, %s, now());
        """
        self.cursor.execute(sql, (sname, kor, eng, mat))
        self.conn.commit()

    def update(self):
        # -- update 테이블명 set 필드1='값1', 필드2='값2', ... where절
        length = self.showAll()

        id = self.getInt(str="수정할 ID >>", round=length, min=1)
        sname = input("이름 >>")
        kor = self.getInt(str="국어 >>")
        eng = self.getInt(str="영어 >>")
        mat = self.getInt(str="수학 >>")

        sql = """
            update tb_score 
            set sname=%s
            , kor=%s
            , eng=%s
            , mat=%s
            , regdate=now() 
            where id=%s;
        """
        self.cursor.execute(sql, (sname, kor, eng, mat, id))
        self.conn.commit()

    def delete(self):
        # -- delete from 테이블명 where id=1
        length = self.showAll()
        id = self.getInt(str="삭제할 ID >>", round=length, min=1)

        sql = """
            delete from tb_score where id=%s;
        """
        self.cursor.execute(sql, (id))
        self.conn.commit()

    def search(self):
        sname = input("검색할 이름 >>")

        sql = """select id, sname, kor, eng, mat
        , (kor+eng+mat) as total
        , ((kor+eng+mat) / 3) as avg
        , date_format(regdate, '%%Y-%%m-%%d %%H:%%i:%%s') as date 
        from tb_score where sname like %s;"""
        
        self.cursor.execute(sql, (f"%{sname}%"))
        rows = self.cursor.fetchall()
        print("-" * 12)
        print("데이터개수", len(rows))
        for row in rows:
            print(f"id: {row['id']}, 이름: {row['sname']}, 국어: {row['kor']}, 영어: {row['eng']}, 수학: {row['mat']}, 총합: {row['total']}, 날짜: {row['date']}")
        

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
        self.conn.close()

    def start(self):
        myFunc = [self.close, self.showAll, self.insert, self.update, self.delete, self.search]
        while True:
            self.showMenu()
            str = "선택 >>"
            sel = self.getInt(str=str, round=len(myFunc)-1)

            myFunc[sel]()

            if sel == 0:
                return
            

if __name__ == "__main__":
    st = SqlTest()
    st.start()
