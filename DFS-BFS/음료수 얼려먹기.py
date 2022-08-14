'''
N # M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
한 번에 만들 수 있는 아이스크림의 개수 출력

ex) 0 0 1 1 0     --> 3개
    0 0 0 1 1
    1 1 1 1 1
    0 0 0 0 0

               (x-1,y)
     (x,y-1)    (x,y)  (x,y+1)
               (x+1,y)
'''

import sys

input = sys.stdin.readline

n,m = map(int,input().split())    # 세로길이 n과 가로길이 m을 입력 받음

graph = []
# 그래프 입력받기
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

'''
graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]

sys.stdin.readline() 는 개행문자를 떼지 않으므로 
rstrip()으로 개행을 없애주어야함
strip()은 공백을 없앰
'''

visited = [[False] * m for _ in range(n)]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False


    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

result = 0

for x in range(n):
    for y in range(m):
            if dfs(x,y) == True:
                result += 1

print(result)