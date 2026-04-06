# 팩토리 패턴 : 객체 생성 책임을 하나의 클래스에게 일임하여 클라이언트에서 호출 시 생성 로직을 몰라도 되도록

from abc import ABC, abstractmethod

# 추상 클래스 정의
class Animal(ABC):
    @abstractmethod
    def speak(self): # Animal을 상속받는 모든 클래스는 speak 함수가 필수로 필요
        pass

# 구체 클래스 정의
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리 클래스
class AnimalFactory:
    def create_new_animal(self, type):
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return None

# 테스트
f = AnimalFactory()
my_dog = f.create_new_animal('dog')
my_dog.speak()