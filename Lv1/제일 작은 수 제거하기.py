'''
# 문제 이해
제일 작은 수 제거하기

'''
def solution(arr):
    answer = []
    min_num = min(arr)
    arr.remove(min_num)
    answer = arr
    if len(arr) == 0:
        answer = [-1]
    return answer
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''