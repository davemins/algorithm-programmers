def solution(progresses, speeds):
    answer = []
    periods = []
    
    for i in range(len(progresses)):
        period = 100 - progresses[i]
        if period % speeds[i] == 0:
            period = period // speeds[i]
        else:
            period = period // speeds[i] + 1
        periods.append(period)
        
    print(periods)
    
    max_period = periods[0]
    count = 1
    
    for i in range(1, len(periods)):
        if periods[i] > max_period:
            answer.append(count)
            count = 1
            max_period = periods[i]
        else:
            count += 1
    
    answer.append(count)
    # count = 1
    # for i in range(len(periods)):
    #     print(i)
    #     if i != len(periods) - 1:
    #         if periods[i + 1] > periods[i]:
    #             answer.append(count)
    #             count = 1
    #         else:
    #             count += 1
    #     else:
    #         answer.append(count)
        
    return answer

'''
# 문제 이해
먼저 남은 진도를 알아보자
그리고 몇 일이 걸리는지 알아보자  -> 확인하면서 작으면 같이, 아니면 다음으로 미루자




# 푼 시간
11:10-

# 채점
오답

# 느낀 점
테스트 통과한 게 27% 밖에 안된다.
if문을 너무 많이 쓴 것 같다.
근데 어디서 논리의 오류가 난 것일까?
아 100일 때를 고려하지 못했다..
-> 그게 아니라 연결되는 최댓값으로 값을 비교하지 않아 생긴 문제이다.
그 전과 비교할 것이 아니라 출발한 값과 비교해야 한다.
'''
