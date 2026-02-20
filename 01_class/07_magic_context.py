"""
07_magic_context.py
주제:
- with 문
- __enter__
- __exit__
"""

import time


class Timer:
    
    # 자원 준비. 시작 시간 측정, 파일 열기 등
    def __enter__(self): 
        """
        TODO:
        시작 시간을 저장하세요.
        """
        self.start = time.time()
        return self
    
    # 자원 정리. 시간 계산, 파일 닫기 등
    def __exit__(self, exc_type, exc_val, exc_tb): 
        """
        TODO:
        종료 시간을 구해서
        실행 시간을 출력하세요.
        """
        end = time.time()
        print(f"실행시간: {end - self.start:.2f}초")
        #pass


if __name__ == "__main__":
    with Timer(): # 시작과 종료 로직을 자동으로 보장해주는 문법
        time.sleep(1)