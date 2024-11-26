'''
# 문제 이해
리스트를 잘 다뤄보자

'''
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[(len(s) // 2) - 1:len(s) // 2 + 1]
    else:
        answer = s[len(s) // 2]
    return answer

'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''