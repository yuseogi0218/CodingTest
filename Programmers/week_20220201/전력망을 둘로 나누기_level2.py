"""
- 하나를 제거하였을 때 개수의 차이를 result list 에 추가
- 제거한 곳에서 부터 출발
"""
from collections import deque


def solution(n, wires: list):
    global graph, ans
    result = list()
    for w in wires:
        graph = [[] for _ in range(n + 1)]
        for wi in wires:
            if w != wi:
                graph[wi[0]].append(wi[1])
                graph[wi[1]].append(wi[0])
        visited = [False] * (n + 1)
        ans = 0
        ans1 = dfs(w[0], visited)
        ans = 0
        ans2 = dfs(w[1], visited)

        result.append(abs(ans1 - ans2))

    return min(result)


def dfs(x, visited):
    global ans
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        if not visited[x]:
            ans += 1
            visited[x] = True
            for i in graph[x]:
                dfs(i, visited)
    return ans


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
