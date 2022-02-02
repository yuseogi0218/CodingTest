N = 0
ans = 0
visited = list()


def solution(k, dungeons: list):
    global N, visited
    N = len(dungeons)
    visited = [False] * N
    dfs(k, dungeons, 0)
    return ans


def dfs(k, dungeons, cnt):
    global ans
    if ans < cnt:
        ans = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, cnt + 1)
            visited[i] = False


solution(80, [[80, 20], [50, 40], [30, 10]])
