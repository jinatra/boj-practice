# 전략패턴: 하나의ㅡ 기능에 대해 여러 전략을 만들어두고, 필요한걸 사용할 수 있도록

# 여러 전략
class Cashpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 현금 결제')

class Cardpayment:
    def pay(self, amount):
        print(f'{amount}원만큼 카드 결제')

# 전략패턴
class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy # 전략을 직접 전달받음
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

cash_service = PaymentService(Cashpayment())
cash_service.checkout(100000)