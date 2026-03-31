# 싱글톤 패턴
# 하나의 클래스가 하나의 인스턴스만을 가짐

class Singleton:
    # 클래스 변수 선언
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)