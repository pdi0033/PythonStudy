# pip install sqlalchemy
# 버전 2.0이상
# https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/2.%20%EC%97%B0%EA%B2%B0%20%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0.html#%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%E1%84%8B%E1%85%AA-%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%AF%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
            "mysql+pymysql://root:1234@localhost:3306/mydb",
            pool_size=10,       # 최대 연결 수
            max_overflow=5,     # 초과 시 추가 연결 수
            pool_recycle=3600   # 재활용 시간
        )

# 1. 데이터 가져오기
with engine.connect() as conn:
    sql = """
        select empno, ename, sal 
        from emp
        """
    result = conn.execute(text(sql))
    for row in result.all():
        print(row)
    
    # dict
    # 한 번 읽으면 끝이라 다시 읽어와야 한다.
    result = conn.execute(text(sql))
    rows = result.mappings().all()
    for row in rows:
        print(dict(row))


# 2. 검색어를 전달할 때.
#ename = input("검색할 이름 : ")
ename = "백승빈"
with engine.connect() as conn:
    sql = """
        select empno, ename, sal
        from emp
        where ename = :name
    """
    # :name
    result = conn.execute(text(sql), [{"name": ename}])
    temp = result.all()
    if len(temp) == 0:
        print("없음")
    else:
        for row in temp:
            print(row)

# 3.insert
with engine.connect() as conn:
    sql = """
        select ifnull(max(empno), 0)+1 
        from emp
        """
    result = conn.execute(text(sql))
    # result.all()은 [(10001), ] 이런 형식으로 온다.
    empno = result.all()[0][0]

    sql = """
        insert into emp(empno, ename, sal)
        values(:empno, :ename, :sal)
        """
    conn.execute(text(sql), [{"empno": empno, "ename": "홍길동"+str(empno), "sal": 9000}])
    #conn.commit()


# 3.insert - 트랜잭션 처리가 안 됨
# with engine.connect() as conn:
#     # test1
#     sql = """
#         select ifnull(max(id), 0)+1
#         from test1
#     """
#     result = conn.execute(text(sql))
#     id = result.all()[0][0]

#     sql = """
#         insert into test1 values(:id, :field)
#     """
#     conn.execute(text(sql), [{"id": id, "field": "test"}])
#     conn.commit()

#     # test2
#     sql = """
#         insert into test2 values(:id, :field)
#     """
#     conn.execute(text(sql), [{"id": id, "field": "12345678901234"}])
    
    
# 3.insert - 트랜잭션 처리
# ACID(atomic, consistancy, isolation, durability)
# 원자성, 일관성, 격리성, 지속성
with engine.begin() as conn:
    # test1
    sql = """
        select ifnull(max(id), 0)+1
        from test1
    """
    result = conn.execute(text(sql))
    id = result.all()[0][0]

    sql = """
        insert into test1 values(:id, :field)
    """
    conn.execute(text(sql), [{"id": id, "field": "test"}])

    # test2
    sql = """
        insert into test2 values(:id, :field)
    """
    conn.execute(text(sql), [{"id": id, "field": "test1234"}])










