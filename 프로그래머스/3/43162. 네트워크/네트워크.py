# 각 컴퓨터는 0부터 n-1인 정수로 표현한다.
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if not visited[j] and computers[i][j]:
                dfs(j)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer