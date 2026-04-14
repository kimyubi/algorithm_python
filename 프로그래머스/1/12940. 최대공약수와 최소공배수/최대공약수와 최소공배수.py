def solution(n, m):
    a, b = n, m
    
    while b != 0:
        a, b = b, a%b
        
    최대공약수 = a
    최소공배수 = (n * m) // a
    return [최대공약수, 최소공배수]
    
