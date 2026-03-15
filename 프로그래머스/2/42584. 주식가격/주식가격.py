def solution(prices):
    
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):

        # 현재 가격이 더 작으면
        # 기다리던 사람들의 가격이 떨어진 것
        while stack and prices[stack[-1]] > prices[i]:

            past = stack.pop()
            answer[past] = i - past

        stack.append(i)

    # 끝까지 가격 안 떨어진 사람들
    while stack:
        past = stack.pop()
        answer[past] = len(prices) - 1 - past

    return answer


# from collections import deque
# def solution(prices):
#     answer = []
#     prices = deque(prices)
    
#     while prices:
#         p = prices.popleft()
#         time = 0
#         for others in prices:
#             time += 1
#             # 가격이 떨어지면
#             if p > others:
#                 break
#         answer.append(time)
            
#     return answer