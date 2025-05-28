# pip install sqlalchemy
# 버전 2.0이상
# https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/2.%20%EC%97%B0%EA%B2%B0%20%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0.html#%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%E1%84%8B%E1%85%AA-%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%AF%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
class ScoreManager:
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

    def output(self):
        # 2.0 이전 버전 conn.execute("쿼리")
        result = self.conn.execute(text("SELECT empno, ename, job, mgr, hiredate, sal, comm, deptno FROM emp"))
        # tuple로 출력한다.
        # for row in result:
        #     print(row)

        # dict으로 출력
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
