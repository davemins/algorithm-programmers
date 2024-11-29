'''
# 문제 이해
약수의 개수에 따라 더할까 뺄까 결정하자


'''
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''