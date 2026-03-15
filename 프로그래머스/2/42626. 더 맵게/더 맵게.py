import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)   

    # 스코빌 지수가 k 미만인 음식이 있는 경우
    while scoville and scoville[0] < K:
        # 음식이 두가지 미만이면 새로운 음식을 만들어 스코빌 지수를 k 이상으로 만들 수 없다.
        if len(scoville) < 2:
            return -1
         
        food_1 = heapq.heappop(scoville)
        food_2 = heapq.heappop(scoville)
        new_food = food_1 + (food_2 * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
        
    return answer