def solution(dartResult):
    tmp = []
    answer = 0
    # 1D2S#10S
    for i, x in enumerate(dartResult):
        if x in ['S', 'D', 'T']:
            number = dartResult[i-1]
            if number == '0':
                if 0 <= i-2 and dartResult[i-2] == '1':
                    number = '10'
            if x == 'S':
                tmp.append(int(number))
            elif x == 'D':
                tmp.append(int(number) ** 2)
            else:
                tmp.append(int(number) ** 3)
                
            if dartResult == '1D2S#10S':
                print(tmp)
            
            if i + 1 < len(dartResult):
                if dartResult[i + 1] == '*':
                    last = tmp.pop() * 2
                    if tmp:
                        first = tmp.pop() * 2
                        tmp.append(first)
                    tmp.append(last)
                elif dartResult[i + 1] == '#':
                    tmp.append(tmp.pop() * -1)
                    
    return sum(tmp)