# n가지 종류의 화폐가 있을 때 화폐들의 개수를 최소한으로 이용해서 그 가치 합이 M원이 되도록 하는 것

# 나의 풀이(해결 x)
n, m = 3, 4
value = [3, 5, 7]
d = [10001 for _ in range(10001)]
d[0] = 0
for v in range(len(value)):
    for i in range(value[v], m+1):
        if d[i-value[v]] != 10001:
            d[i] = min(d[i] ,d[i-value[v]]+1)
if d[i] != 10001:
    print(d[i])
else:
    print(-1)

# 책의 풀이
n, m = map(int,input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
