'''
백준 18352번

어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재한다.
모든 도로의 거리는 1이다. 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오.

첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
둘째 줄부터 M개의 줄에 거쳐 A,B가 주어지며 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다.
'''
import sys

input = sys.stdin.readline

INF = 1e9

n,m,k,x = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신과 거리 0으로 설정
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] == 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        for p in range(1,n+1):
            graph[j][p] = min(graph[j][i] + graph[i][p], graph[j][p])

result = 0
for graph in graph[x]:
    if graph == k:
        result += 1
print(result)
