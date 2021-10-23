import sys

# n과 k를 받습니다.
n, k = map(int, sys.stdin.readline().split())

# 1부터 n까지의 숫자가 담긴 리스트 생성
array = [i+1 for i in range(n)]
# 정답을 담을 리스트
answer = []
# 제거될 숫자의 인덱스
i = 0

# array 리스트에 요소가 존재하는 동안에만 반복
while array:
    i += k-1
    # 만약 i 값이 배열의 길이를 넘어선다면 i를 배열의 길이로 나눠 나온
    # 몫으로 설정
    if i >= len(array):
        i = i % len(array)

    # array에서 i의 인덱스를 가지는 값을 제거하고 answer에 입력
    # join을 쓰기 위해 문자열로 변환하여 입력
    answer.append(str(array.pop(i)))

answer = ", ".join(answer)
print(f"<{answer}>")
