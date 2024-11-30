'''
# 문제 이해
행렬의 덧셈

'''
def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer
'''
# 푼 시간
2분

# 채점
정답

# 느낀 점
없습니다.
'''