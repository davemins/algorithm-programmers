def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        if w < max(size):
            w = max(size)
        if h < min(size):
            h = min(size)
    return w * h

'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다
'''