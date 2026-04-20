from itertools import combinations
def solution(numbers):
    return sorted(list(set([a+ b for a, b in combinations(numbers, 2)])))