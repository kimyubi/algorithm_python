def solution(arr1, arr2):
    answer = [[i + j for i, j in zip(x, y)] for x, y in zip(arr1, arr2)]
    return answer