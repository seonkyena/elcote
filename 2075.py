import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    items = list(map(int, sys.stdin.readline().split()))

    # 맨 처음 리스트가 비어있을 때
    if not heap:
        for item in items:
            heapq.heappush(heap, item)
    # 리스트 안에 요소가 있을 때
    else:
        for item in items:
            # 모든 수는 윗칸의 숫자보다 반드시 크므로 가장 첫번 째 숫자를
            # 기준으로 비교해줘도 무방
            if heap[0] < item:
                heapq.heappush(heap, item)
                # 배열의 길이를 5로 유지
                heapq.heappop(heap)
# 배열 오름차순 정리
heap.sort()
print(heap[0])
