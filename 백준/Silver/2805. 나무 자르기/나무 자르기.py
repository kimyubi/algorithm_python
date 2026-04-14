n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
answer = 0

def check(h):
    total = 0
    for tree in trees:
        if tree > h:
            total += tree - h
            if total >= m: 
                return True
    return False

while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        answer = mid
        left = mid + 1
    
    else:
        right = mid - 1
        
        
print(answer)