# 09:13 am
import sys

# 지방의 수 n
n = int(input())
provinces = list(map(int, input().split()))
total_budget = int(input())
answer = 0


provinces.sort()
# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
if sum(provinces) <= total_budget:
    # 배정된 예산들 중 최댓값인 정수를 출력한다.
    print(provinces[-1])
    sys.exit(0)
    
def check(budget):
    total_cost = 0
    for province in provinces:
        if budget <= province:
            total_cost += budget
        else:
            total_cost += province
            
        if total_cost > total_budget:
            return False
    
    return True
            
        
    
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여
# 그 이상인 예상인 예산 요청에는 모두 상한액을 배정한다.
# left : 예산 요청 최소값 / right : 예산 요청 최대값
left, right = 1, provinces[-1]
while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        left = mid + 1
        answer = mid
    
    else:
        right = mid -1
        
        
print(answer)


    
