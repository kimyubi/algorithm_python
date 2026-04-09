def solution(n):
    answer = ''
    # 0, 2 => 인덱스 짝수 '수'
    #인덱스 홀수 '박'
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer