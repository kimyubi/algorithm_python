n = int(input())
cnt = 0

def is_group(word):
    stack = []
    for c in word:
        if c not in stack:
            stack.append(c)
            continue
        else:
            if stack[-1] == c:
                stack.append(c)
                continue
            else:
                return False
    return True


for _ in range(n):
    word = str(input())
    if is_group(word):
        cnt +=1 
        
print(cnt)