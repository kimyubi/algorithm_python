def solution(n):
    answer = 0
    tmp = ''
    
    while n != 0:
        tmp += str(n % 3)
        n = n // 3
    
    tmp = tmp[::-1]
    for i in range(len(tmp)):
        answer += (3 ** i) * int(tmp[i])
        
    return answer
    
