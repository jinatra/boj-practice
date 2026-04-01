# 팩토리 패턴: 객체 생성을 직접 하지 않고, 팩토리에 맡겨서 대신 만들게 하는 패턴
# 새로운 객체가 추가돼도 팩토리만 수정하면 되므로 확장에 유리

from abc import ABC, abstractmethod

# ──────────────────────────────────────────
# 1. 추상 클래스 (인터페이스 역할)
#    - "Animal을 상속받는 클래스는 반드시 speak()를 만들어야 한다"는 계약
#    - ABC = Abstract Base Class의 약자
#    - 객체들이 같은 메서드를 가진다는 것을 보장하기 위해 사용
# 추상클래스가 하는 말:
# "나는 Animal이 어떻게 생겼는지 정의할게"
# "근데 speak()가 실제로 뭔지는 너네가 정해"
# ──────────────────────────────────────────
class Animal(ABC): # ABC를 상속받아야 추상클래스로 인정됨
    @abstractmethod
    def speak(self):
        pass  # 내용 없음 - 자식 클래스에서 반드시 구현해야 함


# ──────────────────────────────────────────
# 2. 구체 클래스들 (실제로 만들어질 객체)
#    - Animal을 상속받았으니 speak()를 반드시 구현해야 함
#    - 구현 안 하면 인스턴스 생성 시점에 바로 에러
# 구체클래스가 하는 말:
# "알겠어, 나는 Dog고 speak()는 멍멍으로 할게"
# ──────────────────────────────────────────
class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")


# ──────────────────────────────────────────
# 3. 팩토리 클래스 (객체 생성 책임을 전담)
#    - 클라이언트가 Dog(), Cat()을 직접 호출하지 않아도 됨
#    - 새 동물 추가 시 여기만 수정하면 됨 (OCP 원칙)
#    - 반환 타입이 Animal이므로 speak()가 있다는 게 보장됨
# ──────────────────────────────────────────
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("알 수 없는 동물 종류입니다.")  # 잘못된 입력 방어


# ──────────────────────────────────────────
# 4. 사용 (클라이언트 코드)
#    - 팩토리에 문자열만 넘기면 됨
#    - Dog인지 Cat인지 몰라도 speak()는 무조건 있음
# ──────────────────────────────────────────
factory = AnimalFactory()

my_dog = factory.create_animal("dog")
my_dog.speak()  # 멍멍!

my_cat = factory.create_animal("cat")
my_cat.speak()  # 야옹!