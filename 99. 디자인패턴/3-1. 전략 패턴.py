# 전략 패턴: 하나의 기능에 대해 여러 방식(전략)을 만들어두고, 필요할 때 갈아끼우는 패턴

# --- 전략들 (각각의 결제 방식) ---
class CardPayment:
    def pay(self, amount):
        print(f"카드로 {amount}원 결제")

class KakaoPayment:
    def pay(self, amount):
        print(f"카카오페이로 {amount}원 결제")

# --- 컨텍스트 (전략을 갈아끼우는 곳) ---
class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy  # 어떤 전략을 쓸지 받아둠

    def checkout(self, amount):
        self.strategy.pay(amount)  # 받아둔 전략으로 결제 실행

# --- 사용 ---
service = PaymentService(CardPayment())
service.checkout(10000)  # 카드로 10000원 결제

service.strategy = KakaoPayment()  # 전략 교체
service.checkout(5000)   # 카카오페이로 5000원 결제