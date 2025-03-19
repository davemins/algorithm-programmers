def solution(s):
    answer = True
    box = []
    
    for i in s:
        if i == "(":
            box.append(0)
        else:
            if box == []:
                return False
            else:
                box.pop()
    
    if box == []:
        return True
    else:
        return False

'''
# 문제 이해
() 괄호가 잘 짝지어졌을 때 True, 아닐 때 False 출력

# 푼 시간
5분

# 채점
정답

# 느낀 점
맨 처음에는 ")"가 나올 때 box가 비어있을 가능성을 고려하지 않았음
'''
