'''
# 문제 이해
정수 제곱근을 판별하자

'''
import math

def solution(n):
    answer = 0
    sqrt_num = math.sqrt(n)
    if int(sqrt_num) == sqrt_num:
        answer = math.pow(sqrt_num + 1, 2)
    else:
        answer = -1
    return answer
'''
# 푼 시간
6분

# 채점
정답

# 느낀 점
math 라이브러리는 잘 몰랐었다.
이번에 알아간다.
'''