# 전략패턴
# 하나의 기능에 대해 여러 전략을 만들어 둬서, 필요할 때 꺼내서 사용

# 여러 전략들
class CashPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 현금결제')

class CardPayment:
    def pay(self, amount):
        print(f'{amount}원 만큼 카드결제')

# 결제
class PaymentService:
    
    # 메모리에 값이 할당될 떄 사용되는 함수 __init__
    # strategy(전략)을 주입받으면 해당 전략으로 진행
    def __init__(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

card = PaymentService(CardPayment())
card.checkout(10000)