# 전략 패턴
# 하나의 기능에 대해 여러 전략을 만들어두고, 필요할 때 사용

# 전략들
class Cashpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 현금결제')

class Cardpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 카드결제')

# 전략호출
class PaymentService:
    # 객체가 할당된 메모리에 초기값을 설정하는 기본 함수 오버라이드
    def __init__(self, strategy):
        self.strategy = strategy # 전략 주입
    
    def checkout(self, amount):
        self.strategy.pay(amount) # 받아둔 전략으로 결제 실행


service = PaymentService(Cashpayment())

service.checkout(10000)