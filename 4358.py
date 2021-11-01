import sys
from collections import defaultdict

input = sys.stdin.readline
# 디폴트 값이 int
tree = defaultdict(int)
cnt = 0

while True:
    name = input().rstrip()
    if name == "":
        break
    # 값을 지정해주면 그 값이 지정
    tree[name] += 1
    cnt += 1

names = list(tree.keys())
names.sort()

for name in names:
    print("%s %.4f" % (name, tree[name]*100/cnt))
