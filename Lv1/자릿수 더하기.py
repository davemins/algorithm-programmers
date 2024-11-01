'''
# 문제 이해
각 자릿수 더하기

'''
def solution(n):
    answer = 0

    for i in range(len(str(n))):
        answer += int(str(n)[i])

    return answer


'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''