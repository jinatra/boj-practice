# 팩토리 패턴: 객체 생성을 직접 하지 않고, 팩토리를 통해 생성

from abc import ABC, abstractmethod

# 추상클래스 생성
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 구현클래스 생성
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리 (객체 생성 책임)
class AnimalFactory:
    
    def create_animal(self, type):
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return None

factory = AnimalFactory()
my_cat = factory.create_animal('cat')
my_cat.speak()
