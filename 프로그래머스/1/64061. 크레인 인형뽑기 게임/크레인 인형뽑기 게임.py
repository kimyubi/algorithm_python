#-517
def solution(board, moves):
    answer = 0
    machine = []
    stack = []
    for b in zip(*board):
        machine.append(list(reversed(b)))
        
    for move in moves:
        item = machine[move-1]
        
        while item:
            x = item.pop()
            
            # 인형을 뽑았다면
            if x:
                # 같은 모양의 인형 두개가 바구니에 연속해서 쌓인다면
                if stack and stack[-1] == x:
                    stack.pop()
                    answer += 2
                    break
                else:
                    stack.append(x)
                    break
                        
            
    return answer