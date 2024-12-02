
  '''
# 문제 이해
세 숫자의 합이 0이 되는 경우의 수 구하자

'''
def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''
