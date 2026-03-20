def solution(brown, yellow):
    answer = []
    total_block_number = brown + yellow
    for i in range(1, int(total_block_number **0.5) + 1):
        if total_block_number % i == 0:
            a,b = i, total_block_number//i
            c,d = a-2, b-2
            x = a*b - c * d
            if x == brown:
                return(max(a, b), min(a, b))
    return answer