def solutions(n, m):
    for _ in range(m):
        for _ in range(n):
            print('*', end ='')
        print()
    

n, m = map(int, input().strip().split(' '))
solutions(n, m)
