from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        p = prices.popleft()
        cnt = 0
        for others in prices:
            cnt += 1
            if p > others:
                break
        answer.append(cnt)
            
    return answer