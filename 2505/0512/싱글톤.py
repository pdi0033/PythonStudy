class Singleton:
    # 객체를 하나만 만들어야 한다.
    __instance = None   # 객체 만들라고 하면 None일 때만 객체를 만들고
                        # None이 아니면 객체를 반환한다.
    @classmethod
    def getInstance(cls):
        if cls.__instance == None:
            cls.__instance = cls.__new__(cls)
                            # 클래스를 이용해 인스턴스 만들기
        return cls.__instance
    
    def display(self):
        print("*************")

    def __init__(self):
        # 이미 객체가 존재하면 강제 에러를 발생시킨다.
        if Singleton.__instance is not None:
            raise Exception("이 클래스는 반드시 getInstance로만 객체 생성이 가능합니다.")


s1 = Singleton.getInstance()
s1.display()

# 클래스 외부에서 객체를 만드는 것들 파이썬이 막을 방법이 없다.
# 다른 언어들은 생성자한테도 접근 권한이 있어서 이걸 private로 만들면 외부에서 객체 생성을 못한다.
# 파이썬 생성자에 이미 __붙어있어서 별도로 접근 권한을 건드릴 수 없다.

# s2 = Singleton()      # raise Exception으로 설정한 에러가 난다.