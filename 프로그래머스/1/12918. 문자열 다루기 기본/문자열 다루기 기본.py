def solution(s):
    if len(s) in (4, 6):
        for x in s:
            if x.isalpha():
                return False
        return True
    return False