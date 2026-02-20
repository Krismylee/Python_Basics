"""
02_property_setter.py
주제:
- property
- setter
- 값 검증
"""

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = 0
        self.balance = balance  # setter를 통하도록

    @property # 함수지만 변수처럼 쓰게 만드는 문법
    def balance(self):
        return self._balance

    @balance.setter # 속성에 값이 대입될 때 실행되는 함수
    def balance(self, value: int):
        """
        TODO:
        - value가 int가 아니면 TypeError 발생
        - 0보다 작으면 ValueError 발생
        """
        if not isinstance(value, int):
            raise TypeError("balance는 int 타입이어야 합니다.")
        if value < 0:
            raise ValueError("balance는 0 이상이어야 합니다.")

        self._balance = value #### 저장은 _balance로

    def deposit(self, amount):
        self.balance += amount


if __name__ == "__main__":
    acc = BankAccount("홍길동", 1000)
    acc.deposit(500)
    print(acc.balance)

    # 아래를 통과하지 못하도록 수정하세요
    #acc.balance = -100 # ValueError: balance는 0 이상이어야 합니다.
    acc.balance = "a" # TypeError: balance는 int 타입이어야 합니다.