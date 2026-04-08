n = int(input())

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

cnt = 0
for _ in range(n):
    if is_group(str(input())):
        cnt +=1 
        
print(cnt)

