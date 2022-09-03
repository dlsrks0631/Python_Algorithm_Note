'''
< BFS >
1. 처음 방문할 것을 일단 넣는다.
2. 이동한 후 다음 꺼를 또 넣고 반복
'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시작점 (0,0)
visited[0][0] = True    
graph[0][0] = 1

queue = deque()
queue.append((0,0)) # 시작점 삽입

while queue:     
    x,y = queue.popleft()

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        # 벙위를 벗어날 때
        if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:
            continue
            
        # 벽일 때 무시
        if graph[temp_x][temp_y] == 0:
            continue

        if graph[temp_x][temp_y] == 1 and visited[temp_x][temp_y] == False:
            visited[temp_x][temp_y] = True
            graph[temp_x][temp_y] = graph[x][y] + 1
            queue.append((temp_x,temp_y))   # 이동한 후 큐에 삽입

print(graph[n-1][m-1])

