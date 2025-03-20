from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):  
        q.append((priorities[i], i))

    answer = 0

    while q:
        # 현재 큐에서 가장 높은 우선순위 찾기
        max_priority = 0
        for item in q:
            if item[0] > max_priority:
                max_priority = item[0]

        priority, idx = q.popleft()  # 가장 앞에 있는 문서 꺼내기

        if priority == max_priority:  # 가장 높은 우선순위라면 출력
            answer += 1
            if idx == location:  # 찾고 있는 문서가 맞으면 반환
                return answer
        else:
            q.append((priority, idx))  # 우선순위가 낮으면 다시 큐에 넣기


'''
# 문제 이해
특정 프로세스가 몇 번째로 실행되는지 알아보자
우선순위 큐?
i에 인덱스, prioritiesp[i]에 우선순위를 넣는다.
0 1 2 3
2 1 3 2 일 때
0의 우선순위 검사 -> 큰 거 있으면 다시 넣기, 없으면 빼기
우선순위 큐는 아닌 것 같다.

이거 priorities랑 q를 조사해야 할 것 같다.
priorities에 계속 추가하면서 q에 보다 더 큰 우선순위가 있는지 확인하자


# 푼 시간
30분

# 채점
오답

# 느낀 점
일단 큐 라이브러리를 써야 하는지 고민된다.
쓰는 방법 까먹었다..
왜 틀렸을까?
문법이 약해서? 발상 부족으로? 둘 다인 것 같다.
chatGPT에 부분적인 것만 물어봤는데 답을 아예 다 적어준다.
나쁜 놈이다..


# 우선순위 큐 사용법
q = queue.PriorityQueue()

q.put((2, "Task 2"))  # 우선순위 2
q.put((1, "Task 1"))  # 우선순위 1 (더 높은 우선순위)
q.put((3, "Task 3"))  # 우선순위 3

print(q.get())  # (1, "Task 1") 출력
print(q.get())  # (2, "Task 2") 출력
print(q.get())  # (3, "Task 3") 출력

# deque 사용법
from collections import deque

q = deque()  # 리스트 대신 deque 사용

q.append(1)
q.append(2)
q.append(3)

print(q.popleft())  # 1 출력
print(q.popleft())  # 2 출력
print(q.popleft())  # 3 출력

'''
