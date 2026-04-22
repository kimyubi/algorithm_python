def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        x = -1
        for j in range(i):
            if s[i] == s[j]:
                x = i-j
        answer.append(x)
    return answer