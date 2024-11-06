'''
# 문제 이해
주어진 숫자를 나누었을 때 나머지가 1이 되는 최솟값 구하기

'''
def solution(n):
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''