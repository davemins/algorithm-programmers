'''
# 문제 이해
두 정수 사이의 합을 구하자.

'''
def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b + 1):
            answer += i
    else:
        for i in range(b, a + 1):
            answer += i
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''