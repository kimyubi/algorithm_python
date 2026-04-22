def solution(a, b, n):
    answer = 0
    # 보유 중인 빈병이 n개 이상일 때
    while n >= a:
        exchanged = n // a
        answer += exchanged * b
        n = exchanged * b + (n % a)
    
    return answer