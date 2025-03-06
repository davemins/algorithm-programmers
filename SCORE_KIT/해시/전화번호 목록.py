'''
# 문제 이해
한 번호가 다른 번호의 접두어?
어떤 번호가 다른 번호의 접두어 -> false
그렇지 않으면 -> true

각 전화번호의 길이는 1 이상 20 이하

먼저 정렬을 한 후에 하나씩 넣어가면서 비교하면 어떨까?
접두어가 되기 위한 조건 : 첫 번째 숫자가 같아야 한다


'''
def solution(phone_book):
    phone_book.sort(reverse = True)
    phone_book_list = [[] for i in range(10)]
    
    for num in phone_book:
        idx = int(num[0])
        if len(phone_book_list[idx]) > 0 :
            for book in phone_book_list[idx]:
                # if num in book: # 아마 여기에서 틀린 것 같다.. 그 시작하는 것을 판단하도록 바꾸자
                if book.startswith(num):
                    return False
        else:
            phone_book_list[idx].append(str(num))
            print(phone_book_list)
    return True

'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
짜증나는 게 phone_book_list와 비교해야 하는데 phone_book이랑 비교해서 자꾸 시간 낭비했다..
내가 만든 리스트의 이름은 확실히 구분되게 해보자.
접두어 관계라면 반드시 인접한 위치에 정렬이 되기에 굳이 phone_book_list를 사용할 필요가 없었다.
너무 복잡하게 풀고 있었던 것 같다.. 고민의 시간을 조금만 더 늘이자. 15분 고민?

# 최종 풀이
def solution(phone_book):
    phone_book.sort()  # 오름차순 정렬 (작은 값부터)
    
    for i in range(len(phone_book) - 1):  # 마지막 요소는 비교할 필요 없음
        if phone_book[i + 1].startswith(phone_book[i]):  # 바로 다음 번호와 비교
            return False  # 접두어가 존재하면 False 반환

    return True  # 접두어가 없으면 True

'''
