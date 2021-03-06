## 그래프
- 기본 구조
    - 노드 = 정점
    - 간선
        - 두 노드를 연결 함
    - 두 노드는 인접하다
        - 두 노드가 간섭으로 연결됨

- 표현 방식-1
    - 인접 행렬
        - 2차원 배열(리스트)로 그래프의 연결관계를 표현하는 방식
        - 노드 - 행, 열
        - 간선 - 데이터
            - 자기자신 - 0
            - 연결된 노드 
                - 간선 값
            - 연결 되어 있지 않은 노드
                - 무한 = 999999999 or 987654321


```python
# 무한의 비용 선언
INF = 999999999

# 2차원 배열로 그래프 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
```

- 표현 방식-2
    - 인접 리스트
        - 리스트로 그래프의 연결관계를 표현하는 방식
        - 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
        - 구현
            - 2차원 리스트 이용


```python
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 간선)
graph[0].append((1,7)) # 노드 0,1 은 간선 7에 의해 연결되어있다.
graph[0].append((2,5))

graph[1].append((0,7)) # 노드 1,0 은 간선 7에 의해 연결되어있다.

graph[2].append((0,5))

print(graph)
```

    [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
    

- 두 표현 방식 비교
    - 메모리 측면
        - 인접 행렬 방식 > 인접 리스트 방식
            - 인접 행렬 방식은 모든 관계를 저장
            - 인접 리스트 방식은 연결된 정보만을 저장 -> 메모리를 효율적으로 사용
    - 읽는 속도
        - 인접 행렬 방식 < 인접 리스트 방식
            - 인접 리스트 방식은 연결된 데이터를 하나씩 확인

## DFS - 깊이 우선 탐색
- Depth-First-Search
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조에 기초 + 재귀함수 이용
- 데이터의 개수가 N개인 경우 시간복잡도 - O(N)
- 방법
    - 1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    - 2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있는지 확인
        - 2-1) 있으면
            - 그 인접 노드를 스택에 넣고 방문 처리를 한다.
                - 번호가 낮은 순대로 한다.
        - 2-2) 없으면 
            - 스택에서 최 상단 노드를 꺼냄
   - 3)  2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


```python
# 구현 - 인접 리스트 방식의 그래프
def dfs(graph, v, visited):
    # - 그래프, 시작 노드, 각 노드가 방문된 정보)
    
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ") # 노드의 탐색 순서 출력
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: # i = 현재 노드와 연결된 다른 노드
        if not visited[i]: # 방문 안했던 노드 이면
            dfs(graph, i,visited) # 재귀함수로 반복 시행
                # 종료 조건
                    # - visited[i] == True 일때 - 모두 방문 했을때
                    
# graph
graph = [
    [], # 0노드 없음
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
        
```

    1 2 7 6 8 3 4 5 

## BFS - 너비 우선 탐색
- Breadth First Search
- 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조를 이용
- 방법
    - 1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    - 2) 큐에서 노드를 꺼냄
        - 2-1) 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입후 방문 처리
            - 방문하지 않은 노드들중 작은 노드들 부터 큐에 삽입
    - 3) 2번 과정을 더이상 수행할 수 없을 때까지 반복


```python
# 구현 - 인접 리스트 방식의 그래프
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 시작 노드를 큐에 삽입
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = " ")
        
        # 해당 노드의 인접 노드중 방문 하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # 모두 방문 처리
                visited[i] = True
                

graph = [
    [], # 0노드 없음
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
        
```

    1 2 3 8 7 4 5 6 
