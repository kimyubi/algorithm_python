def solution(name):
    n = len(name)
    answer = 0

    # 알파벳 변경 비용
    for c in name:
        up = ord(c) - ord('A')
        down = ord('Z') - ord(c) + 1
        answer += min(up, down)

    # 커서 이동 비용
    move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        move = min(
            move,
            2 * i + (n - next_idx),
            i + 2 * (n - next_idx)
        )

    return answer + move