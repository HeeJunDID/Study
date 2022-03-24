import sys
from collections import deque
import heapq
INF = int(1e9)
sys.stdin = open('ex4.txt')
input = sys.stdin.readline
n, m, c = map(int,input().split())
start = c
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
cnt = 0
max_num = 0
for i in range(1, len(distance)):
    if i == start:
        continue
    elif distance[i] != INF:
        cnt += 1
        if max_num < distance[i]:
            max_num = distance[i]
print(cnt, max_num)