# 3x 마을 사람들은 3을 저주의 숫자라고 생각한다.
# 그래서 3의 배수와 숫자 3을 사용하지 않는다.
#
# 10진법 → 3x 마을 숫자 대응표:
# 1→1, 2→2, 3→4, 4→5, 5→7, 6→8, 7→10, 8→11, 9→14, 10→16
#
# 정수 n이 주어질 때, 3x 마을에서 사용하는 숫자로 바꿔 return
#
# 입출력 예:
# n=15 → 25
# n=40 → 76

def solution(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if num % 3 != 0 and '3' not in str(num): # 유효한 수(3의 배수가 아니고 3 포함 X)일때만 count를 올림
            count += 1
    return num

print(solution(4))