import sys
sys.stdin = open('./ex1.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    print(int(input()))