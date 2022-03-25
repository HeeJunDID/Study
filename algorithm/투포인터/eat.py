import sys
sys.stdin = open('sol.txt')
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    a = map(int,input().split())
    b = map(int,input().split())
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    a_start, b_start = 0,0
    cnt = 0
    while a_start < len(a) and b_start < len(b):
        if a[a_start] > b[b_start]:
            print(a[a_start], b[b_start])
            cnt += 1
            b_start += 1
            if b_start == m:
                a_start += 1
                b_start = 0
        else:
            a_start += 1
            b_start = 0
    print(cnt)