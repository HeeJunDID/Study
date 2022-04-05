import sys

sys.stdin = open("ex3.txt")
input = sys.stdin.readline

n = int(input())
mat = []
total = 0
for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        # 위치, 초
        shaq_loc = [i, temp.index(9), 0]
    mat.append(temp)
    total += sum(temp)
# 위치, 초, 매트릭스, 성장 카운트
shaq_loc.append(mat)
shaq_loc.append(0)
total -= 9
shaq_size = 2


def can_go(mat):
    state = False
    for i in range(n):
        for j in range(n):
            if 0 < mat[i][j] < shaq_size:
                state = True
                break
    return state


cnt_list = []
if total == 0:
    print(0)
else:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = [shaq_loc]
    while stack:
        x, y, sec, mat, growing_cnt = stack.pop()
        if can_go(mat):
            if total == 0:
                break
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] <= shaq_size:
                    if 0 < mat[nx][ny] < shaq_size:
                        mat[nx][ny] = 0
                        total -= mat[nx][ny]
                        growing_cnt += 1
                        if growing_cnt == shaq_size:
                            shaq_size += 1
                            growing_cnt = 0

                    stack.append((nx, ny, sec + 1, mat, growing_cnt))

        else:
            cnt_list.append(sec)
            print(cnt_list)
print(cnt_list)
