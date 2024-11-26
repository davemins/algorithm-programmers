'''
# 문제 이해
핸드폰 번호를 바꾸자

'''
def solution(phone_number):
    answer = phone_number[-4:]
    secret_num = '*' * (len(phone_number) - 4)
    answer = secret_num + answer
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''
