# 싱글톤 패턴: 하나의 클래스에 하나의 인스턴스만 생성되도록 하는 패턴
# IO가 많은 작업등에 용이

class Singleton:
    _instance = None # 아직 인스턴스 없음
    
    # 메모리에 객체가 할당될 때 쓰이는 함수에 오버라이드
    def __new__(cls):
        if cls._instance is None: # 객체 없으면
            cls._instance = super().__new__(cls) # 새로 생성
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)