def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key = lambda x : x[1])
    
    def dfs(current, cnt):
        if cnt == len(tickets):
            answer.append(current)
            return True
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                visited[i] = True
                answer.append(current)
                if dfs(tickets[i][1], cnt + 1):
                    return True
                
                answer.pop()
                visited[i] = False
        
        return False
    dfs("ICN", 0)
    return answer