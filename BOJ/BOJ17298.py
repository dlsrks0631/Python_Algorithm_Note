# 4
# 3 5 2 7 ---> 5 7 7 -1
# lst1 lst2 lst3 lst4  result = [-1, -1, -1, -1]

from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

lst = list(map(int,sys.stdin.readline().rstrip().split()))
# lst = [3,5,2,7]

result = [-1] * n # 결과값

for i in range(n):
    for j in range(i+1,n):
        if lst[i] < lst[j]:
            result.popleft()
            result.append(lst[j])

# for i in range(n):
#     while True:
#         if lst[i+1] > lst[i]:
#             result.append(lst[i+1])
#             break
#         else:
#             i += 1

for j in result:
    print(j,end = ' ')