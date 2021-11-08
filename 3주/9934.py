import sys

input = sys.stdin.readline

K = int(input())
data = list(map(int, input().split()))
# 함수 안에서 따로 리턴을 안해주므로 미리 선언, K번 출력해야하니 K개의 리스트를 포함한 리스트를 선언
result = [[] for _ in range(K)]


def slovenia(data, x):
    global result  # 전역 함수 사용
    mid = (len(data)//2)  # 데이터 길이의 절반 값
    # 배열의 중간값이 루트 노드이고 루트 노드를 제외한 좌우측의 값들은 서브트리라고 생각하고 재귀를 사용한다.
    # x의 값이 레밸이자 result 배열의 인덱스가 된다.
    result[x].append(data[mid])
    if len(data) == 1:  # 받은 배열의 길이가 1일 시에는 종료
        return
    slovenia(data[:mid], x+1)   # 깊이(인덱스)를 1 증가시켜 반환한다.
    slovenia(data[mid+1:], x+1)


slovenia(data, 0)

for i in range(K):
    print(*result[i])
