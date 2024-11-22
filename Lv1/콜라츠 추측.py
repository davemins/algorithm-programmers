'''
# 문제 이해
1이 될 때까지 반복하는 문제다.

'''
def solution(num):
    answer = 0
    for _ in range(500):
        if num == 1:
            break

        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1

    if num != 1 and answer > 1:
        answer = -1

    return answer
'''
# 푼 시간
10분

# 채점
정답

# 느낀 점
분기에서 어떻게 나뉠지 생각하고 문제가 길어도 꼼꼼히 읽어 조건을 모두 확인하자
'''