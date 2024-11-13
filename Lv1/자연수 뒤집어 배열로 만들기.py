'''
# 문제 이해
자연수 뒤집어 배열로 만들기

'''
def solution(n):
    answer = []
    str_n = str(n)
    for i in range(len(str_n)):
        answer.append(int(str_n[len(str_n) - i - 1]))
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''