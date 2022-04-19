import sys

sys.stdin = open("./ex1.txt")
input = sys.stdin.readline
fish_map = []
for _ in range(4):
    temp = list(map(int, input().split()))
    f_tmp = []
    for i in range(2, len(temp) + 1, 2):

        f_tmp.append(temp[i - 2 : i])

    fish_map.append(f_tmp)

shark_loc = (0, 0)
dx = [
    -1,
]
dy = [
    0,
]
