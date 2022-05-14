import sys
from collections import deque

sys.stdin = open('./maze.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int,list(input().strip()))))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque([[0,0]])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
            queue.append((nx,ny))
            maze[nx][ny] = maze[x][y] + 1
print(maze[n-1][m-1])

