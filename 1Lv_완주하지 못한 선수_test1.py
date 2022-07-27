def solution(participant, completion):
    answer = ''
    
    for i in participant:
        pn = participant.count(i)
        cn = completion.count(i)
        if i not in completion : answer = i
        elif pn > cn : answer = i
    
    return answer
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (6.76ms, 10.2MB)
테스트 4 〉	통과 (26.70ms, 10.4MB)
테스트 5 〉	통과 (26.68ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
채점 결과
정확성: 50.0
효율성: 0.0
합계: 50.0 / 100.0

'''
