'''
# 문제 이해
이전 숫자를 확인하자


'''
def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if t[i:i + len(p)] <= p:
            answer += 1
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''