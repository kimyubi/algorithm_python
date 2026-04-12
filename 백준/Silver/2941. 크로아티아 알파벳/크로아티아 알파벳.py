x = input()
alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0

i = 0
while i < len(x):
    if x[i:i+2] in alpha:
        i += 2
    elif x[i:i+3] == 'dz=':
        i += 3
    else:
        i += 1
    answer += 1

print(answer)
        
    