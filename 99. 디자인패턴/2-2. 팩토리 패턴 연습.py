# 팩토리 패턴
# 객체 생성 책임을 하나의 클래스(팩토리)에게 일임하여 클라이언트에서 클래스 생성 로직을 몰라도 되게 하도록

from abc import ABC, abstractmethod

# 추상 클래스
class Animal(ABC):
    # 추상메서드를 speak에 선언하여 추후 Animal을 상속받는 클래스는 speak 가 필수
    @abstractmethod
    def speak(self):
        pass

# 구체 클래스
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리 클래스
class AnimalFactory:
    # 객체 생성 함수
    def create_animal(self, type: str) -> Animal:
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            pass

factory = AnimalFactory()
my_dog = factory.create_animal('dog') # 동물을 생성할 때 각 class 별로 들어가서 어떻게 객체 생성해야되는거 알 필요 없이 AnimalFactory만 호출하면됨
my_dog.speak()
