# 가로의 길이가 N 세로의 길이 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을 1 x 2의 더ㅠ개, 2 x 1의 덮개, 2 x 2의 덮개를 이용해 채우고자 한다.

# 나의 풀이 해결(x)
n = 3
d = [0 for _ in range(1001)]
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    if n % 2 == 0:
        d[i] = d[i-2] + 3
    else:
        d[i] = d[i-1] + 1
print(d[n] % 796796)

# 책의 풀이

n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 *d[i-2]) % 796796
print(d[n])