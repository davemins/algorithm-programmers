'''
# 문제 이해
모두 완주
완주하지 못한 선수의 이름을 return
동명이인도 고려해야 한다.
'''
def solution(participant, completion):
    result = {}
    for item in completion:
        result[item] = result.get(item, 0) + 1
    
    for item2 in participant:
        if result.get(item2, 0) == 0:
            return item2
        else:
            result[item2] -= 1
'''
# 푼 시간
11분

# 채점
오답

# 처음 짠 코드
-> 효율성 테스트 시간 초과..
def solution(participant, completion):
    for i in completion:
        participant.remove(i) -> arrayList여서 아마 시간 초과가 나오는 것 같다..
    
    return participant[0]
    
리스트가 2개 있다. for문을 지양하자..
map을 사용해보자!

# 다음 짠 코드
-> 효율성 테스트 시간 초과
def solution(participant, completion):
    result = {}
    answer = ""
    for item in completion:
        result[item] = result.get(item, 0) + 1
    
    for item2 in participant:
        if item2 in completion:
            if result[item2] == 0:
                answer = item2
                break
            result[item2] -= 1
        else:
            answer = item2
            break
        
    return answer

# 마지막 짠 코드
def solution(participant, completion):
    result = {}
    for item in completion:
        result[item] = result.get(item, 0) + 1
    
    for item2 in participant:
        if result.get(item2, 0) == 0:
            return item2
        else:
            result[item2] -= 1
            
# 느낀 점
문법에 많이 약함..
딕셔너리 사용법 익혀두자
그리고 코드부터 치는 습관을 버리자
심사숙고해서 생각을 정리하고 풀이를 시작하자
'''
