'''
신고 시스템


k번 이상 신고되면 정지
id_list에 사용자 목록 입력됨
report에 muzi frodo 이런 식으로 신고자 + 대상자 형태의 문자열로 표시

'''


def solution(id_list, report, k):

    result = []
    for value in report:
        if value not in result:
            result.append(value)
    
    
    answer = [0 for i in range(len(id_list))]
    
    a = []
    b = []
    c = []

    for i in result:
        a.append(i.split(' ')[0])

    for j in result:
        b.append(j.split(' ')[1])

    for m in b:
        if b.count(m) >= k:
            c.append(m)

    for n in range(len(b)):
        if b[n] in c:
            for m in range(len(id_list)):
                if id_list[m] == a[n]:
                    answer[m] += 1

    return answer

list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(list ,report, 2))
    
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (28.94ms, 10.6MB)
테스트 7 〉	통과 (69.24ms, 10.7MB)
테스트 8 〉	통과 (86.03ms, 11.2MB)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (3.56ms, 10.2MB)
테스트 13 〉	통과 (1.20ms, 10.3MB)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	통과 (1.11ms, 10.2MB)
테스트 17 〉	통과 (1.07ms, 10.3MB)
테스트 18 〉	통과 (7.08ms, 10.1MB)
테스트 19 〉	통과 (18.40ms, 10.2MB)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.4MB)
채점 결과
정확성: 66.7
합계: 66.7 / 100.0

'''
