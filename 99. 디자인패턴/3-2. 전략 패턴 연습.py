# 전략패턴
# 하나의 기능에 대해 여러 전략을 만들어두고 필요할때 사용할 수 있도록 함

# 여러 전략들
class CashPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 현금결제')

class CardPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 카드결제')


# 구현 서비스
class PaymentService:
    
    # __new__로 생성된 객체에 속성(프로퍼티)을 세팅
    # 전략들을 주입받았을 때 실제 메모리 내부에 값을 할당하도록 함
    def __init__(self, strategy):
        self.strategy = strategy # 이제 메모리 내에 strategy라는 초기값이 할당됨
    
    def checkout(self, amount):
        self.strategy.pay(amount) # self(자기자신)에 주입받은 전략의 pay 함수 사용

# 테스트
svc = PaymentService(CardPayment())
svc.checkout(10000)