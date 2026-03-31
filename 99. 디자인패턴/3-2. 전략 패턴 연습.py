# 전략패턴
# 하나의 기능에 대해 여러가지 전략을 만들어두고 원할때 쓸 수 있게 하는 패턴

# 개별전략들
class CashPayment:
    def pay(self, amount):
        print(f'{amount}원만큼 현금 결제합니다')

class CardPayment:
    def pay(self, amount):
        print(f'{amount}원만큼 카드결제합니다.')

# 전략패턴
class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy # 전략 주입받기

    def checkout(self, amount):
        return self.strategy.pay(amount)

# 구현
cash_pay = PaymentService(CashPayment())
cash_pay.checkout(1000)