import sys

N = int(sys.stdin.readline())

for i in range(N):
    X = input()
    s = []
    for j in X:
        if j == '(':
            s.append(j)
        elif j == ')':
            if len(s) == 0:
                s.append(j)
            elif s[-1] == '(':
                s.pop()

    if len(s) == 0:
        print('YES')
    elif len(s) > 0:
        print('NO')
