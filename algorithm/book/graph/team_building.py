import sys

sys.stdin = open('team_building.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
print(parent)
# for _ in range(m):
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    c, a, b = map(int,input().split())
    if c == 0:
        union(parent, a, b)
    elif c == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
