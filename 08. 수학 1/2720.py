import sys

def change_calaulator(money: int):
    while True:
        q = money // 25
        money = money - q*25
        d = money // 10
        money = money - d*10
        n = money // 5
        money = money - n*5
        p = money // 1
        money = money - p*1
        break
    print(q, d, n, p)

T = int(sys.stdin.readline())
for _ in range(T):
    money = int(sys.stdin.readline())
    change_calaulator(money)
