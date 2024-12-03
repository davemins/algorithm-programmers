'''
# 문제 이해
문자열과 숫자의 변환\

'''
def solution(s):
    s_list = list(map(int, s.split()))
    answer = str(min(s_list)) + ' ' + str(max(s_list))
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''