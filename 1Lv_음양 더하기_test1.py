'''
정수들의 절댓값

'''
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
            
    
    return answer

a = [4, 7, 12]
b = [True,False,True]

print(solution(a, b))
