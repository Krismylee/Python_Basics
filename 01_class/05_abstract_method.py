"""
05_abstract_method.py
주제:
- ABC
- abstractmethod
- 인터페이스 개념
"""

from abc import ABC, abstractmethod # ABC = Abstact Base Class


class Animal(ABC):

    @abstractmethod # 직접 객체를 생성하지 않고 자식 클래스의 규칙만 정의
    def speak(self):
        pass


class Dog(Animal):
    """
    TODO:
    speak 메소드를 구현하세요.
    "멍멍"을 출력하도록 하세요.
    """
    def speak(self):
        print("멍멍")
    #pass


class Cat(Animal):
    """
    TODO:
    speak 메소드를 구현하세요.
    "야옹"을 출력하도록 하세요.
    """
    def speak(self):
        print("야옹")
    #pass


if __name__ == "__main__":
    d = Dog()
    d.speak()

    c = Cat()
    c.speak()