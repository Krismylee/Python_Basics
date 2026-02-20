"""
01_basic_class.py
주제:
- 클래스 기본 구조
- 인스턴스 메소드
- 클래스 변수
- __repr__
"""

class Employee:
    company = "LGCNS"  # 클래스 변수. 모든 객체가 공유

    # 생성자. 객체가 만들어질 때 자동으로 실행. 입력된 각 직원의 개별 정보 저장
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    def introduce(self):
        """
        TODO:
        아래 형식으로 문자열을 반환하도록 수정하세요.
        예시:
        "안녕하세요. AI팀의 홍길동(28)입니다."
        """
        return f"안녕하세요. {self.team}팀의 {self.name}({self.age})입니다."
        #pass

    def change_team(self, new_team): # 팀 변경 메서드
        self.team = new_team

    # 클래스 호출 시 자동 실행. 객체를 출력할 때 보여지는 형태 정의. 디버깅용.
    def __repr__(self): 
        """
        TODO:
        디버깅에 도움이 되는 형태로 수정하세요.
        예시:
        Employee(name='홍길동', age=28, team='AI')
        """
        return f"Employee(name='{self.name}', age={self.age}, team='{self.team}')" # "Employee 객체"


if __name__ == "__main__":
    emp = Employee("홍길동", 28, "AI") # 객체 저장
    print("Company: ", emp.company)
    print(emp)
    print(emp.introduce())
    print("--------------Change Team--------------")
    emp.change_team("AI클라우드")
    print(emp)
    print(emp.introduce())