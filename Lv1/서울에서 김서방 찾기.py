'''
# 문제 이해
서울에서 김서방 찾기

'''
def solution(seoul):
    location = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            location = i
            break
    answer = "김서방은 " + str(location) + "에 있다"
    return answer
'''
# 푼 시간
2분

# 채점
정답

# 느낀 점
없습니다.
'''