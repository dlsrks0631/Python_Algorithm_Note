# BFS -> 너비 우선 탐색 / 가까운 노드부터 탐색하는 알고리즘

'''
큐를 사용하면 인접한 노드를 반복적으로 큐에 넣으면 자연스럽게 먼저 돌아온 것이 먼저 나가게 된다.
1. 시작 노드를 큐에 삽입 후 방문처리
2. 큐에서 노드를 꺼내 방문하지 않은 인접 노드를 모두 큐에 삽입
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
'''

from collections import deque

def bfs(graph,start,visited):
    queue= deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited) # 시작노드 1