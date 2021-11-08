import sys

input = sys.stdin.readline

# 두 수를 곱한 뒤 최대공약수로 나누는 함수


def LCM(a, b):
    return (a * b) // GCD(a, b)

# 두 수의 최대공약수를 구하는 함수


def GCD(a, b):
    if b % a:
        return GCD(b % a, a)
    else:
        return a


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))
