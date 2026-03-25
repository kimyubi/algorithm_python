from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    
    for r in rectangle:
        # 좌측 하단 x1, 좌측 하단 y1 / 우측 상단 x2, 우측 하단 y2
        x1, y1, x2, y2= map(lambda x : x*2, r)
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if y1 < i < y2 and x1 < j < x2:
                    graph[i][j] = 1
                if graph[i][j] != 1:
                    graph[i][j] = 0
    
    queue = deque()
    queue.append((cx, cy, 1))
    visited[cy][cx] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, d = queue.popleft()
        
        if (x, y) == (ix, iy):
            return d // 2
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not visited[ny][nx] and not graph[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, d + 1))
        
    
    return answer