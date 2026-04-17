# 싱글톤 패턴
# 하나의 클래스가 하나의 객체만을 가짐
# 공유 자원의 중복 생성 방지

class Singleton:
    # 클래스 인스턴스
    _instance = None
    
    # 객체가 생성되어 메모리에 할당될 때 호출되는 기본함수
    # 해당 함수를 오버라이드하여 싱글톤 패턴 구현
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)