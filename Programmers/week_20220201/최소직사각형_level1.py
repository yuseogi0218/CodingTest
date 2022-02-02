"""
큰 값을 모두 가로, 작은 값을 모두 세로
"""


def solution(sizes):
    w, h = 0, 0
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
        if w < s[0]:
            w = s[0]
        if h < s[1]:
            h = s[1]

    return w * h


solution([[60, 50], [30, 70], [60, 30], [80, 40]])
