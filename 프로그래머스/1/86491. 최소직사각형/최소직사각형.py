def solution(sizes):
    for s in sizes:
        s.sort()
        
    return max([s[0] for s in sizes]) * max([s[1] for s in sizes])
        
    
