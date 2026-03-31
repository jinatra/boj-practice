# 싱글톤 패턴: 하나의 클래스에 하나의 인스턴스만을 가짐

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)

class NoSingle:
    pass

c = NoSingle()
d = NoSingle()

print(c is d)