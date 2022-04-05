import sys

sys.stdin = open('city_plan.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
house = [i for i in range(n+1)]
print(house)


def find(house, x):
    if house[x] != x:
        house[x] = find(house, house[x])
    return house[x]


def union(house, a, b):
    a = find(house, a)
    b = find(house, b)
    if a < b:
        house[b] = a
    else:
        house[a] = b


for _ in range(m):
    a, b, c = map(int, input().split())
    union(house, a, b)
print(house)
