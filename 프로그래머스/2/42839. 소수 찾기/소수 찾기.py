from itertools import permutations
def is_prime(item):
    if item < 2:
        return False
    
    for i in range(2, int(item**0.5) + 1):
        if item % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(map(int, numbers))
    set_n = set()
    
    for i in range(1,len(numbers) + 1):
        for n in permutations(numbers, i): 
            n = int("".join(list(map(str, n))))
            set_n.add(n)            
            
    for item in set_n:
        if is_prime(item):
            answer += 1
    return answer