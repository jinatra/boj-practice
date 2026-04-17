# 팩토리 패턴
# 객체 생성 책임을 하나의 클래스에 일임하도록 하여 클라이언트에서 객체생성할 때 각 클래스별 객체 생성 로직을 모두 알지 않아도 되게

from abc import ABC, abstractmethod

# 추상 클래스
# ABC를 주입하여 추상클래스임을 알게함
class Animal(ABC):
    # abstractmethod를 선언하여 Animal을 상속받는 모든 클래스들은 speak 함수를 정의해야함
    @abstractmethod
    def speak(self):
        pass

# 구체 클래스
# 실제로 객체 생성에 사용될 실물 클래스들
class Dog(Animal):
    def speak(self):
        print('walf')

class Cat(Animal):
    def speak(self):
        print('meow')

# 팩토리 클래스
class AnimalFactory:
    # 객체 생성 함수
    def create_animal(self, type):
        if type == 'dog':
            return Dog()
        elif type == 'cat':
            return Cat()
        else:
            raise ValueError()

# 테스트
ftry = AnimalFactory()
my_dog = ftry.create_animal('dog') # 이제 객체 생성할때는 ftry 하나만 있어도 되므로 편함
my_dog.speak() # Animal 상속 클래스들은 모두 speak 함수가 있다는걸 알고있으므로 바로 쓸 수 있다
