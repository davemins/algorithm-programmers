# from itertools import combinations
# from math import prod

def solution(clothes):
    dic_clothes = {}

    for cloth in clothes:
        if cloth[1] not in dic_clothes:
            dic_clothes[cloth[1]] = 0
        dic_clothes[cloth[1]] += 1
  
    combinations = 1
    for count in dic_clothes.values():
        combinations *= (count + 1)
    
    return combinations - 1


#     total_sum = 0
#     values = list(dic_clothes.values())
#     n = len(values)
    
#     for r in range(1, n+1):
#         for comb in combinations(values, r):
#             total_sum += prod(comb)
    
#     return total_sum
'''
# 푼 시간
30분

# 채점
오답

# 문제 이해
조합 문제

n(a+b+c)일 때 -> n + a * b * c

먼저 종류 별로 담아야 한다

# 느낀 점
곰곰히 생각하면 결국 답이 보인다
'''
