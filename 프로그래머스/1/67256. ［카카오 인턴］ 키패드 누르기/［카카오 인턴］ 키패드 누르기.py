# BFS
from collections import deque
def solution(numbers, hand):
    answer = ''      
    
    phone = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]
               
    left, right = '*', '#'
    def distance(start, end):
        sx, sy, ex, ey = 0,0,0,0
        for i in range(4):
            for j in range(3):
                if phone[i][j] == start:
                    sx, sy = i, j
                if phone[i][j] == end:
                    ex, ey = i, j
        return abs(sx-ex) + abs(sy-ey)
    
    for num in numbers:
        num = str(num)
        if num in ['1', '4', '7']:
            answer += 'L'
            left = num
            continue
        elif num in ['3', '6','9']:
            answer += 'R'
            right = num
            continue
        else:
            left_distance = distance(left, num)
            right_distance = distance(right, num)
            
            # 왼쪽손이 더 가까운 경우
            if left_distance < right_distance:
                answer += 'L'
                left = num
                continue
            # 오른손이 더 가까운 경우
            elif left_distance > right_distance:
                answer += 'R'
                right = num
                continue
            # 두 손가락 거리가 같다면 오른손 잡이는 오른 손가락, 왼손잡이는 왼 손가락
            else:
                if hand == 'right':
                    answer += 'R'
                    right = num
                    continue
                else:
                    answer += 'L'
                    left = num
                    continue
            
    return answer
    
