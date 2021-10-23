import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    X = input()
    # 입력 받은 문자열을 구분하여 해당되는 if문 실행
    if X == 'top\n':
        if arr:
            print(arr[-1])
        else:
            print(-1)

    elif X == 'pop\n':
        if arr:
            print(arr.pop())
        else:
            print(-1)

    elif X == 'size\n':
        print(len(arr))

    elif X == 'empty\n':
        if arr:
            print(0)
        else:
            print(1)

    else:
        # push의 경우 push\n 이후 숫자들을 입력
        arr.append(int(X[5:]))
