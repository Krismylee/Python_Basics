"""
06_magic_call.py
주제:
- __call__
- 객체를 함수처럼 사용
"""

class Multiplier:

    def __init__(self, number):
        self.number = number

    def __call__(self, value): # 객체를 상태를 가진 함수처럼 쓰게 해주는 매직 메서드
        """
        TODO:
        value * self.number 를 반환하도록 수정하세요.
        """
        return value * self.number


if __name__ == "__main__":
    m = Multiplier(10) # 입력에 10을 곱하는 곱셈처리함수 생성
    print(m(5))  # 5 * 10 = 50