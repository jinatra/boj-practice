# 싱글톤 패턴: 하나의 클래스에 하나의 인스턴스만 가짐

class Singleton:
    # 클래스 변수: 만들어진 인스턴스를 여기에 저장
    _instance = None
    
    # 객체가 메모리에 할당될때
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)