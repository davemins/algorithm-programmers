'''
# 문제 이해
종류에 따라 폰켓몬 존재, 가질 수 있는 종류 수의 최댓값
종류의 개수 구하기 => N/2과 비교해 가질 수 있는 종류 수의 최댓값 구하기
N / 2 >= 종류의 개수 : 종류의 개수가 값
나머지 : N / 2
'''
def solution(nums):
    
    nums_set = set(nums)
    
    if len(nums) // 2 > len(nums_set):
        answer = len(nums_set)
    else:
        answer = len(nums) // 2
    
    return answer

'''
# 푼 시간
11분

# 채점
정답

# 느낀 점
set에 대한 발상이 괜찮았던 것 같다.
처음에 count(nums_set)을 사용해서 오류가 났다. 문법에 대한 익숙함을 기르자.
answer = 0 이거 나중에 정의하니까 굳이 처음에 안 써도 괜찮다.
'''
