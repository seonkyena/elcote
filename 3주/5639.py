import sys

sys.setrecursionlimit(10**9)  # 메모리 한도 증가
input = sys.stdin.readline

preorder = []  # 원래 루트를 위한 리스트

while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(start, end):
    if start >= end:
        return

    root = preorder[start]

    if preorder[end - 1] <= root:
        postorder(start + 1, end)
        print(root)
        return

    for i in range(start + 1, end):
        if preorder[i] > root:
            idx = i
            break

    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)


postorder(0, len(preorder))
