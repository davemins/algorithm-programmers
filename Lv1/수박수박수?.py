'''
# 문제 이해
n만큼 수박 출력하기

'''
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
'''
# 푼 시간
2분

# 채점
정답

# 느낀 점
없습니다.
'''