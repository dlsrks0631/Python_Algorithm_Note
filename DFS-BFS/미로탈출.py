'''
동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 시작 칸과 마지막 칸을 모두 포함하여 계산
'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어났을 때 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽일 때 무시
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
        



