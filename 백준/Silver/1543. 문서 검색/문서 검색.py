doc = input()
word = input()

n = len(word)
answer, idx = 0, 0


while idx <= len(doc):
    if doc[idx: idx+n] == word:
        answer += 1
        idx += n
    else:
        idx += 1
        
print(answer)
    