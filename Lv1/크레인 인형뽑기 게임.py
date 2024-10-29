'''
# 문제 이해
인형 뽑기 중 사라진 인형의 수를 구하자.

# 발상
구현하자.

# 복잡도
board 배열의 높이를 k, 뽑기 횟수를 n이라고 할 떄 O(kn)의 시간복잡도를 가진다.

'''
def solution(board, moves):
    answer = 0
    bag = [] # 바구니 리스트
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0:
                # 바구니로 이동
                bag.append(board[j][i])
                board[j][i] = 0
                # 같이 인형이 연달아 뽑혔을 때 제거
                n = len(bag) - 1
                if n >= 1 and bag[n - 1] == bag[n]:
                    answer += 2
                    bag.pop()
                    bag.pop()
                break
    return answer
'''
# 푼 시간
3분

# 채점
정답

# 느낀 점
없습니다.
'''