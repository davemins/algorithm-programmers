def solution(genres, plays):
    answer = []
    genres_plays = {}  # 장르별 총 재생 수
    genres_num = {}    # 장르별 (재생 수, 인덱스) 저장

    # 1. 장르별 총 재생 수 및 곡 정보 저장
    for i in range(len(genres)):
        if genres[i] not in genres_plays:
            genres_plays[genres[i]] = 0
            genres_num[genres[i]] = []
        genres_plays[genres[i]] += plays[i]
        genres_num[genres[i]].append((plays[i], i))  # (재생 수, 인덱스) 저장

    # 2. 장르별 총 재생 수 기준 내림차순 정렬
    sorted_genres = sorted(genres_plays.keys(), key=lambda x: genres_plays[x], reverse=True)

    # 3. 각 장르에서 재생 수 내림차순, 인덱스 오름차순으로 정렬 후 2개씩 뽑기
    for genre in sorted_genres:
        # (재생 수 내림차순, 인덱스 오름차순) 정렬
        sorted_songs = sorted(genres_num[genre], key=lambda x: (-x[0], x[1]))
        
        # 상위 2곡 추가
        answer.extend([idx for _, idx in sorted_songs[:2]])

    return answer

'''
# 내가 구현을 진행한 부분까지의 코드

def solution(genres, plays):
    answer = []
    genres_plays = {}
    genres_num = {}
    
    for i in range(len(genres)):
        if genres[i] not in genres_plays:
            genres_plays[genres[i]] = 0
            genres_num[genres[i]] = []
        genres_plays[genres[i]] += plays[i]
        genres_num[genres[i]].append(i)
    
    genres_plays = dict(sorted(genres_plays.items(), key=lambda x:x[1], reverse=True))
    
    # 여기서 내림차순 장르 내(genres_plays)로 내림차순 2곡을 뽑으려면 어떻게 해야 할까?
    for genre in genres_plays.keys():
        for i in genres_num[genre]:
            answer.append(i)
    
    return answer
'''
'''
# 문제 이해
장르별로 2개
수록 기준 -> 일단 장르 별로 나누기 -> 장르의 총 재생 횟수 구해기 -> 장르 안의 곡 정렬하기 -> 총 재생 횟수 내림차순으로 2개씩 뽑아 answer에 넣기

고민해보자, genres_plays ={"classic" : 2300}
genres_num = {"classic" : [0, 2, 3]}

인덱스를 어떻게 처리하면 좋을까? -> 차례대로가 아닌 한번에 넣는 로직을 고민해보자

# 푼 시간
11:09

# 채점
오답

# 느낀 점
엄청 어렵다라는 생각보다 파이썬 문법 활용 능력이 많이 떨어져서 아쉽다는 생각 뿐이다..
일단 해시를 마치게 되었기에 감사합니다.
'''
