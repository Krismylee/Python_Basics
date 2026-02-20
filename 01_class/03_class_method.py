"""
03_classmethod.py
주제:
- classmethod
- 대체 생성자
"""

class User:

    default_role = "USER"

    def __init__(self, name, role=None):
        self.name = name
        self.role = role if role else self.default_role

    @classmethod # 객체가 아니라 클래스 자체를 기준으로 동작하는 메서드. 대체 생성자
    def from_string(cls, text):
        """
        TODO:
        "이름,역할" 형식의 문자열을 받아서
        User 객체를 생성하도록 완성하세요.
        예:
        "홍길동,ADMIN"
        """
        name, role = text.split(",")
        print(name, role) # split된 결과 출력
        return cls(name, role)
        #pass

    @classmethod
    def change_default_role(cls, new_role):
        cls.default_role = new_role


if __name__ == "__main__":
    user = User("김영희")
    print(user.name, user.role) # 김영희 USER. role 입력이 없으므로 default role 출력
    User.change_default_role("GUEST") 
    u = User("김철수")
    print(u.name, u.role) # 김철수 GUEST. 바뀐 default role 적용

    u2 = User.from_string("홍길동,ADMIN") # string 분리
    print(u2.name, u2.role) # 새로운 객체. name과 role 모두 입력값 적용