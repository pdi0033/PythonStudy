# 주급계산
# 아이디
# 이름
# 근무시간
# 시간당급여액
# 연장수당 - case when문 근무시간 > 20
import pymysql
import pymysql.cursors

class PayCal:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',    # ip localhost = 127.0.0.1
                       user='user01',         # 아이디
                       password='1234',     # 패스워드
                       db='mydb',           # 데이터베이스명
                       port=3306) 
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        sql = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = 'mydb'
            AND TABLE_NAME = 'tb_payment';
            """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            sql = """
                create table tb_payment(
                id bigint primary key auto_increment,
                ename varchar(20) not null,
                work_time int not null,
                time_pay int not null,
                bonus_pay int not null,
                regdate datetime );
            """
            self.cursor.execute(sql)
            self.conn.commit()

    def isInt(self, s):
        try:
            int(s)
        except ValueError:
            return False
        return True

    def getInt(self, str="", round = 100000000000000, min = 0):
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
        sql = """select id, ename, work_time, time_pay, bonus_pay
        , (work_time * time_pay + 
            CASE
                WHEN work_time > 20 THEN (work_time - 20) * (time_pay / 2)
                ELSE 0
            END) AS total
        , date_format(regdate, '%Y-%m-%d %H:%i:%s') as date 
        from tb_payment;"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print("-" * 12)
        print("데이터개수", len(rows))
        for row in rows:
            print(f"id: {row['id']}, 이름: {row['ename']}, 근무시간: {row['work_time']}, 시간당 급여액: {row['time_pay']:,d}, 추가수당: {int(row['bonus_pay']):,d}, 총합: {int(row['total']):,d}, 날짜: {row['date']}")
        
        return len(rows)
    
    def insert(self):
        ename = input("이름 >>")
        work_time = self.getInt(str="근무시간 >>")
        time_pay = self.getInt(str="시간당 급여액 >>")

        sql = """
            insert into tb_payment(ename, work_time, time_pay, regdate)
            values(%s, %s, %s, now());
        """
        self.cursor.execute(sql, (ename, work_time, time_pay))
        self.conn.commit()

    def update(self):
        # -- update 테이블명 set 필드1='값1', 필드2='값2', ... where절
        length = self.showAll()

        id = self.getInt(str="수정할 ID >>", round=length, min=1)
        ename = input("이름 >>")
        work_time = self.getInt(str="근무시간 >>")
        time_pay = self.getInt(str="시간당 급여액 >>")

        sql = """
            update tb_payment 
            set ename=%s
            , work_time=%s
            , time_pay=%s
            , regdate=now() 
            , bonus_pay=%s
            where id=%s;
        """
        self.cursor.execute(sql, (ename, work_time, time_pay, id))
        self.conn.commit()

    def delete(self):
        # -- delete from 테이블명 where id=1
        length = self.showAll()
        id = self.getInt(str="삭제할 ID >>", round=length, min=1)

        sql = """
            delete from tb_payment where id=%s;
        """
        self.cursor.execute(sql, (id))
        self.conn.commit()

    def search(self):
        ename = input("검색할 이름 >>")

        sql = """select id, ename, work_time, time_pay
        , case 
            when work_time > 20 then (work_time-20) * (time_pay / 2)
            else 0
        end as bonus_pay
        , (work_time * time_pay + 
            CASE
                WHEN work_time > 20 THEN (work_time - 20) * (time_pay / 2)
                ELSE 0
            END) AS total
        , date_format(regdate, '%%Y-%%m-%%d %%H:%%i:%%s') as date 
        from tb_payment
        where ename like %s;"""
        
        self.cursor.execute(sql, (f"%{ename}%"))
        rows = self.cursor.fetchall()
        print("-" * 12)
        print("데이터개수", len(rows))
        for row in rows:
            print(f"id: {row['id']}, 이름: {row['ename']}, 근무시간: {row['work_time']}, 시간당 급여액: {row['time_pay']:,d}, 추가수당: {int(row['bonus_pay']):,d}, 총합: {int(row['total']):,d}, 날짜: {row['date']}")
        

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
    pc = PayCal()
    pc.start()