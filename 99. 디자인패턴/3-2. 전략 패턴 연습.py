# 전략패턴
# 하나의 기능에 대해 여러 전략을 만들고 필요한 전략만 필요할 때 쓸 수 있게 하는 패턴

# 여러 전략들
class CashPayment:
    def pay(self, amount):
        print(f'{amount}원만큼 현금결제')

class CardPayment:
    def pay(self, amount):
        print(f'{amount}원만큼 카드결제')

# 실제 서비스
class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy # 인자로 전략 주입
    
    def checkout(self, amount): # 주입된 전략에 따라 pay 함수 실행
        return self.strategy.pay(amount)

# 테스트
card_pay = PaymentService(CardPayment())
card_pay.checkout(2000)