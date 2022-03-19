# 정수 X가 주어질 때 X에 사용할 수 있는 연산방법 4가지를 활용하여 1을 만드는데 이때 연산을 사용하는 횟수의 최솟값을 출력하라

# 나의 풀이
def solution(n):
    d = [0 for _ in range(30000)]
    d[0] = 0
    d[1] = 0
    for i in range(2, n+1):
        if i % 5 == 0:
            d[i] = min(d[i -1], d[i//5]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i-1], d[i//3]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i-1], d[i//2]) + 1
        else:
            d[i] = d[i-1] + 1
    return d[i]
print(solution(26))

# 책의 풀이

x = int(input())   

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])

