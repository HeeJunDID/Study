# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 위와 같이 소스 코드를 작성하면 n이 커질수록 수행 시간이 기하 급수적으로 늘어난다.

