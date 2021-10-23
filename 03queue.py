import sys

input = sys.stdin.readline

N = int(input())
arr = []
# front 인덱스를 가리킴
cnt = 0

for i in range(N):
    X = input()
    # 배열의 길이가 인덱스의 값보다 클 때만 출력
    # 작다면 이 배열은 빈 것으로 간주
    if X == 'front\n':
        if len(arr) > cnt:
            print(arr[cnt])
        else:
            print(-1)
    elif X == 'back\n':
        if len(arr) > cnt:
            print(arr[-1])
        else:
            print(-1)
    # 배열의 길이가 인덱스의 값보다 클 때만 출력
    # cnt 보다 작은 인덱스의 값을 pop 된 것으로 간주
    # 출력 후 pop한 것으로 간주하여 인덱스 값 1 증가
    elif X == 'pop\n':
        if len(arr) > cnt:
            print(arr[cnt])
            cnt += 1
        else:
            print(-1)
    # 현재 배열의 길이에서 cnt의 값 뺀 값
    # cnt의 값이 0 보다 크다면 pop 된 요소가 있는 것
    elif X == 'size\n':
        print(len(arr)-cnt)
    # 현재 배열의 길이와 cnt의 값이 같다면 이 배열은 빈 것임
    # 1을 출력하고 리스트와 cnt 값 초기화
    elif X == 'empty\n':
        if len(arr) == cnt:
            print(1)
            arr = []
            cnt = 0
        else:
            print(0)

    else:
        arr.append(int(X[5:]))
