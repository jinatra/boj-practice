# 팩토리패턴
# 객체생성 책임을 팩토리 클래스만 전담하게하여 클라이언트에서 객체를 생성할 때 각 객체별로 알지 않아도 되도록

from abc import ABC, abstractmethod

# 추상클래스
class Animal(ABC):
    # Animal을 상속받는 모든 객체는 speak라는 함수를 정의하도록 명시
    @abstractmethod
    def speak(self):
        pass

# 구체 클래스
class Cat(Animal):
    def speak(self):
        print('meow')

class Dog(Animal):
    def speak(self):
        print('walf')

class AnimalFactory:
    
    def create_animal(self, type):
        if type == 'cat':
            return Cat()
        elif type == 'dog':
            return Dog()
        else:
            raise ValueError()

f = AnimalFactory()
my_dog = f.create_animal('dog')
my_dog.speak()