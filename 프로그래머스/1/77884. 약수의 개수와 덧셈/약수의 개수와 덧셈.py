def solution(left, right):
    answer = 0
    
    # 약수의 개수가 짝수이면 True, 홀수이면 False 리턴
    def calculator(number):
        cnt = 0
        for i in range(1, number + 1):
            if not number % i:
                cnt += 1
        return not cnt % 2
    
    for x in range(left, right + 1):
        if calculator(x):
            answer += x
        else:
            answer -= x
                
    return answer