import pymysql
import pymysql.cursors

# 추상성 - 클래스 내부구조 몰라도 사용하게 하는 성격
class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',       # ip localhost = 127.0.0.1. localhost - loop back 주소
            user='user03',          # 아이디
            password='1234',        # 패스워드
            db='project1',          # 데이터베이스명
            port=3306               # port, 프로세스 식별값. 프로세스 안에 소켓이라는 객체가 있음.
                                    # 소켓-통신을 담당하는 라이브러리
                                    # 소켓에 부여된 번호가 port이다.
                                    # 2byte정수 1~655535까지 가능하다. 1~1000은 함부로 못씀.
                                    # 80 - http(웹서버). www.daum.net:80
                                    # 21 - telnet
                                    # 22 - ssh
                                    # 23 - ftp
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # insert, update, delete
    def execute(self, query, args=()):
        # args - tuple 기본값
        print(args)
        self.cursor.execute(query, args)
        self.db.commit()

    # 데이터 딱 한개만 가져오기
    # scalar 쿼리 포함. select count(*) from tb_memver
    def executeOne(self, query, args=()):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row      # 결과를 반환해야 한다. 첫 번째 레코드 값 하나만 가져간다.
    
    # 데이터 여러 개 가져오기
    def executeAll(self, query, args=()):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows

    def close(self):    # 닫기
        if self.db.open:
            self.db.close()



