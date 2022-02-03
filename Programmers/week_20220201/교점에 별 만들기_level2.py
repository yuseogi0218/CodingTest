"""
- 주어진 선들의 모든 교점을 구한다.
"""


def solution(line):
    result = list()
    point = list()
    xs = list()
    ys = list()
    for l in line:
        A, B, E = l[0], l[1], l[2]
        for m in line:
            C, D, F = m[0], m[1], m[2]
            # 교점이 존재할 경우
            if A * D - B * C != 0:
                x = (B * F - E * D) / (A * D - B * C)
                y = (E * C - A * F) / (A * D - B * C)
                if x % 1 == 0 and y % 1 == 0 and point.count([x, y]) != 1:
                    xs.append(int(x))
                    ys.append(int(y))
                    point.append([int(x), int(y)])

    max_x, max_y, min_x, min_y = max(xs), max(ys), min(xs), min(ys)

    for j in range(max_y, min_y - 1, -1):
        ts = ""
        for i in range(min_x, max_x + 1):
            if point.count([i, j]) == 1:
                ts += "*"
            else:
                ts += "."
        result.append(ts)

    return result


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
