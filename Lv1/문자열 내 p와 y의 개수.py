'''
# 문제 이해
대소문자 구분 없이 개수 비교하기

'''
def solution(s):
    answer = True
    if s.count("p") + s.count("P") == s.count("y") + s.count("Y"):
        answer = True
    else:
        answer = False
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''