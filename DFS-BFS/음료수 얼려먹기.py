'''
N # M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
한 번에 만들 수 있는 아이스크림의 개수 출력

ex) 0 0 1 1 0     --> 3개
    0 0 0 1 1
    1 1 1 1 1
    0 0 0 0 0

< 문제 해결 >
(0,0) 부터 시작해서 상 하 좌 우를 확인하며 방문하지 않았으며 구멍이 뚫려 있으면 방문처리
그리고 상 하 좌 우를 확인했는데 방문을 한 것이거나 칸막이가 존재하지 않는 경우 결과값을 1씩 더하자
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

print(graph)
print(visited)
