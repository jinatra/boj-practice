# 팩토리 패턴
# 객체 생성 책임을 별도의 객체(팩토리)로 분리하여 클라이언트가 구체 클래스에 의존하지 않도록
# 하는 패턴

from abc import ABC, abstractmethod

# 추상객체
class Animal(ABC): # ABC를 통해 추상객체임을 선언
    @abstractmethod
    def speak(self): #추상메서드 선언함으로서 Animal을 상속받는 클래스는 모두 speak 함수를 생성해야함
        pass

# 실체객체
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리
class AnimalFactory:
    # 객체 생성 함수 하나로 관리
    def create_animal(self, type:str) -> Animal:
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            return None

# 구현
factory = AnimalFactory()
new_dog = factory.create_animal('dog')
new_dog.speak()

