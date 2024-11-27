
'''
# 문제 이해
문자열을 검사하자.

'''
def solution(s):
    answer = True
    if len(s) in [4, 6] and s.isnumeric():
        pass
    else:
        answer = False
    return answer
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
isnumeric() 처음 알았습니다.
'''
