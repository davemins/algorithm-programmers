'''
# 문제 이해
정수 배열과 부호 배열을 통해 결과를 구하기

# 발상
구현해보자.

# 복잡도
입력 값의 개수가 n일 때 O(n)의 시간복잡도를 가진다.

'''
def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''