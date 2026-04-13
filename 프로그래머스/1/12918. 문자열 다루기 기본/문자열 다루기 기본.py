def solution(s):
    if len(s) not in (4, 6):
        return False
    for x in s:
        if x.isalpha():
            return False
            
    return True