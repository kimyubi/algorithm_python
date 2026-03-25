#1016
def solution(new_id):
    x = set('-_.~!@#$%^&*()=+[{]}:?,<>/') - set('-_.')
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for c in new_id:
        if c in x:
            new_id = new_id.replace(c, '')
                
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4단계
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:  
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # 5단계
    if not new_id:
        new_id = 'a'
        
    # 6단계 
    if 16 <= len(new_id):
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <=2:
        while True:
            if len(new_id) == 3:
                break
            new_id += new_id[-1]
        
    return new_id
