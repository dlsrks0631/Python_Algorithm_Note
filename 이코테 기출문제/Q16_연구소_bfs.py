import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [] # 맵 입력받을 곳
n_graph = [[0] * m for _ in range(n)] # 벽을 설치하고 난 뒤 모습

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 방향 = [상,하,좌,우]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0