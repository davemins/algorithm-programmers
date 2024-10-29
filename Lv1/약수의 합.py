'''
# 문제 이해
정수 n의 약수를 모두 더한 값을 구하자.

# 발상
구현해보자.

# 복잡도
입력값이 n일 때 O(n)의 시간복잡도를 가진다.

'''
def solution(n):
	answer = 0
	for i in range(1, n + 1):
		if n % i == 0:
			answer = answer + i
	return answer

print(solution(12))
'''
# 푼 시간
1분

# 채점
정답

# 느낀 점
없습니다.
'''