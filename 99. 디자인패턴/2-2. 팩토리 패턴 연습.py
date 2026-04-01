# 팩토리 패턴
# 객체 생성 책임을 하나의 클래스(팩토리)에 위임하여 클라이언트 클래스에서 구체 클래스들을 알지 않아도 객체 생성 가능

from abc import ABC, abstractmethod

# 추상 클래스 정의
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 구체 클래스 정의
class Dog(Animal):
    def speak(self):
        print(f'walf')

class Cat(Animal):
    def speak(self):
        print(f'meow')

# 팩토리 클래스
class AnimalFactory:
    def create_animal(self, type):
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return None

# 구현
factory = AnimalFactory()
my_cat = factory.create_animal('cat')
my_cat.speak()