# 이미 가지고 있는 랜선의 개수 k, 필요한 랜선의 개수 n
k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]

answer = 0

def check(length):
    total = 0
    for wire in wires:
        total += (wire // length)
        if n <= total:
            return True
    return False
        

left, right = 1, max(wires)
while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)