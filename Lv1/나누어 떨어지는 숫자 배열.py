'''
# 문제 이해
나누어 떨어지는 숫자 배열

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
3분

# 채점
정답

# 느낀 점
없습니다.
'''