'''
input:
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
from pprint import pprint

# 정점 개수, 간선 개수
V, E = map(int, input().split())
# 간선 정보 저장
data = list(map(int, input().split()))

# 인접 행렬 개수
adj_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]  # 0 인덱스를 사용하지 않기 위해 더미 집어넣기

# 간선 정보 입력
# 간선이 8개기 때문에 간선 개수만큼 반복
for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

pprint(adj_matrix)


def DFS(start):
    stack = [start]
    # 스택이 비었다는건 더 탐색할 곳이 없다는 것
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited[current_node] = 1

            # 어떻게 다음 곳으로?
            # 현재 노드와 인접한 노드가 누구인지 매트릭스에서 찾아야 함.
            # V부터 1까지 역순으로 확인해야 작은 번호가 스택의 위쪽에 위치하고 정방향 탐색이 가능해지기 때문
            for next_node in range(V, 0, -1):


    pass
