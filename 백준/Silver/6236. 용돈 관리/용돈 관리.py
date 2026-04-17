n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]

left = max(moneys)
right = sum(moneys)

answer = 0

def check(k):
    account = k
    cnt = 1
    
    for money in moneys:
        if account < money:
            account = k
            cnt += 1
        
        account -= money
        
        if m < cnt:
            return False
        
    return True

while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        answer = mid
        right = mid - 1
        
    else:
        left = mid + 1
print(answer)