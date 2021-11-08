import sys

input = sys.stdin.readline
N, K = map(int, input().split())

eratos = [True] * (N+1)  # 0번 인덱스는 없음
cnt = 1

for i in range(2, N+1):
    if eratos[i] == True:  # 값이 True 일 때
        for j in range(i, N+1, i):  # j부터 i의 배수만큼
            if eratos[j] == False:  # 값이 False라면 반복문으로 돌아감
                continue

            if cnt == K:
                print(j)

            eratos[j] = False  # 숫자가 체에 걸러질 때마다 cnt 값 증가
            cnt += 1
