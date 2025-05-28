from DBModule import Database

def output():
    db = Database()     # 객체 만들면 이미 디비 접근
    sql = "select * from tb_member"
    rows = db.executeAll(sql)
    for row in rows:
        print(row)
    db.close()

# 회원가입
def member_register():
    db = Database()
    user_id = input("아이디 >>")
    # if not idCheck(user_id):    # 사용 못하는 상황
    #     print("이미 사용중인 아이디 입니다.")
    #     return                  # 강사님 코드
    if check_id(user_id) == False:
        return
    
    password = input("패스워드 >>")
    user_name = input("이름 >>")
    email = input("이메일 >>")
    phone = input("전화 >>")

    sql = """
        insert into tb_member(user_id, password, user_name, email, phone, regdate)
	    values(%s, %s, %s, %s, %s, now())
    """
    db.execute(sql, (user_id, password, user_name, email, phone))
    db.close()

# 아이디 중복 체크
# 아이디 입력받고 나서 디비에 이미 존재하는지
# 존재하면 '이미 존재하는 아이디입니다.'하고 끝
# '사용가능한 아이디입니다.'출력하고 나머지 입력받아 회원가입
def check_id(user_id=""):
    if user_id == "":
        print("아이디를 입력해주세요.")
        return False
    
    db = Database()
    sql = "select count(*) cnt from tb_member where user_id=%s"
    row = db.executeOne(sql, (user_id))
    cnt = row["cnt"]
    db.close()

    if cnt > 0:
        print("이미 존재하는 아이디입니다.")
        return False
    
    print("사용 가능한 아이디입니다.")
    return True

def idCheck(user_id=""):
    if user_id == "":       # 에러 체크
        print("아이디를 입력해주세요.")
        return False
    
    sql = "select count(*) cnt from tb_member where user_id=%s"
    db = Database()
    row = db.executeOne(sql, (user_id))
    cnt = row["cnt"]

    db.close()
    if cnt == 0:
        return True     # 중복 안 됐으니까 쓸 수 있다
    return False

if __name__ == "__main__":
    member_register()
    output()

