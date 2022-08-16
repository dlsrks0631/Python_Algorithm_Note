'''
백준 18352번

1. 아이디어
2. 시간복잡도
3. 자료구조
'''


from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque()
q.append(x)

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)