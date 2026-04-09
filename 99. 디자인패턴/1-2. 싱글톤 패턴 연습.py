# 싱글톤 패턴
# 하나의 클래스에 하나의 인스턴스만 존재

class Singleton:
    # 클래스 변수: 만들어진 인스턴스를 저장
    _instance = None
    
    # 객체를 메모리에 생성하는 단계
    # 싱글톤 패턴을 위해 기존 __new__ 함수를 오버라이드
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)