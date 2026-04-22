def solution(food):
    answer = ''
    for food_num, cnt in enumerate(food[1:]):
        if cnt == 1:
            continue
            
        else:
            answer += str(food_num + 1) * (cnt//2)
    answer = answer + '0' + answer[::-1]
    return answer