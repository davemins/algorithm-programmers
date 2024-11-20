'''
# 문제 이해
하샤드 수인지 판별하자

'''
def solution(x):
    answer = True
    total = 0
    for i in range(len(str(x))):
        total += int(str(x)[i])
    if x % total != 0:
        answer = False
    return answer
'''
# 푼 시간
2분

# 채점
정답

# 느낀 점
없습니다.
'''