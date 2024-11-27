def solution(s):
    answer = True
    if len(s) in [4, 6] and s.isnumeric():
        pass
    else:
        answer = False
    return answer
