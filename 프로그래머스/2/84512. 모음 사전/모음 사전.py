from itertools import product
def solution(word):
    answer = sorted([''.join(x) for i in range(1, 6)
              for x in list(product(['A', 'E', 'I', 'O', 'U'], repeat = i))])
    
    return answer.index(word) + 1