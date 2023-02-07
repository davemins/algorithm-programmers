def solution(board, moves):
    answer = 0
    bag = [] # 바구니 리스트
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0:
                bag.append(board[j][i])
                board[j][i] = 0
                n = len(bag) - 1
                if n + 1 >= 2 and bag[n - 1] == bag[n]:
                    answer += 2
                    bag.pop(); bag.pop()
                break
    return answer
