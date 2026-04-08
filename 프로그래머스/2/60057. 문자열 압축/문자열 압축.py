from collections import Counter
import sys
def solution(s):
    answer = sys.maxsize
    
    # n개 단위로 문자열을 잘라 압축
    for n in range(1, len(s)//2 + 2):
        # n개 단위로 문자열을 잘랐을 때, 문자열의 집합
        words = []
        for i in range(0, len(s), n):
            words.append(s[i:i+n])
            
        result = ''
        tmp, prev = 0, None
        for c in words:
            if not prev:
                tmp += 1
                prev = c
                continue
            
            if prev == c:
                tmp += 1
                continue
            else:
                if tmp == 1:
                    result += prev
                else:
                    result += (str(tmp) + prev)
                prev = c
                tmp = 1
                
        if tmp == 1:
            result += prev
        else:
            result += (str(tmp) + prev)
        answer = min(answer, len(result))
        
    return answer