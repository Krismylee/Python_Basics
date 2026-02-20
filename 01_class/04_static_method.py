"""
04_staticmethod.py
주제:
- staticmethod
- 인스턴스/클래스와 무관한 유틸 함수
"""

class Validator:

    @staticmethod # 클래스 안에 있지만 클래스도 객체도 전혀 사용하지 않는 함수
    def is_email(value):
        """
        TODO:
        - 문자열인지 확인
        - '@'가 포함되어 있는지 확인
        - 간단한 이메일 형식 검증 구현
        """
        # 문자열 확인
        if not isinstance(value, str) :
            return False
        # '@' 포함 확인
        if "@" not in value:
            return False
        # 간단한 이메일 형식 검증 구현
        local, _, domain = value.partition("@")
        if not local or not domain:
            return False
        if "." not in domain:
            return False
        tld = domain.split(".")[-1]
        if not tld:
            return False

        return True


if __name__ == "__main__":
    print(Validator.is_email("test@test.com")) # True
    print(Validator.is_email("invalid-email")) # False
    print(Validator.is_email("abcd@ef")) # False
    print(Validator.is_email("abcd@efg.")) # False