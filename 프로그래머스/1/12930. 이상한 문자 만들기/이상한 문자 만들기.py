def solution(s):
    result = ''
    idx = 0
    for c in s:
        # 공백을 만나면 공백 그대로 result에 추가해주고, idx를 0으로 초기화 시킨다.
        if c == ' ':
            result += c
            idx = 0
        else:
            if not (idx % 2):
                result += c.upper()
            else:
                result += c.lower()
            
            idx += 1
    return result

