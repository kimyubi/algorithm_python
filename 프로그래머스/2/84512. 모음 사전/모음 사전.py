from itertools import product
def solution(word):
    answer = 0
    e = []
    dict = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        x = list(product(dict, repeat =i))
        for f in x:
            e.append(''.join(f))
    e.sort()
    print(e)
    return e.index(word) + 1