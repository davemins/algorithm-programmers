'''
# 문제 이해
부족한 금액을 계산하자

'''
def solution(price, money, count):
    answer = -1
    
    total_price = 0
    
    for i in range(1, count + 1):
        total_price += price * i
    
    if money >= total_price:
        answer = 0
    else:
        answer = total_price - money

    return answer
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''
