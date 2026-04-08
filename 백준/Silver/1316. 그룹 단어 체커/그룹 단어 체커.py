n = int(input())
cnt = 0

def is_group(word):
    seen = set()
    prev = None
    
    for c in word:
        if c != prev:
            if c in seen:
                return False
            seen.add(c)
            prev = c
    return True


for _ in range(n):
    word = str(input())
    if is_group(word):
        cnt +=1 
        
print(cnt)

