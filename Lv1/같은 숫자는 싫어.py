'''
# 문제 이해
이전 숫자를 확인하자


'''
def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)

    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''