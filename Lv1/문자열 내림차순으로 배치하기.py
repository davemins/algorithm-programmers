'''
# 문제 이해
리스트를 다뤄보자

'''
def solution(s):
    answer = ''
    s_list = []
    for i in range(len(s)):
        s_list.append(s[i])
    s_list.sort(reverse = True)
    for i in range(len(s)):
        answer += s_list[i]
    return answer

'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''