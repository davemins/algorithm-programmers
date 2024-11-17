'''
# 문제 이해
정수 내림차순으로 배치하기
'''


def solution(n):
    n_str = str(n)
    answer = 0
    array = []
    answer_str = ''

    for i in range(len(n_str)):
        array.append(n_str[i])

    array.sort(reverse=True)

    for i in range(len(array)):
        answer_str += array[i]

    answer = int(answer_str)

    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''