# 전략 패턴: 하나의 기능에 대해 여러 전략들을 만들어놓고 필요할 때 사용

# 여러 전략들
class Cashpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 현금 결제')

class Cardpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 카드 결제')

# 전략 호출
class PaymentService:
    # 객체가 생성되고 메모리에 할당될 때, 전달받은 strategty를 주입받도록
    def __init__(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

# 테스트
card_pay = PaymentService(Cardpayment())
card_pay.checkout(20000)