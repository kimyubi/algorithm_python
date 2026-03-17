def solution(answers):
    answer = []
    f = [1, 2, 3, 4, 5]
    s = [2, 1, 2, 3, 2, 4, 2, 5]
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    
    for (i, a) in enumerate(answers):
        if a == f[i%5]:
            score[0] += 1
        if a == s[i%8]:
            score[1] += 1
        if a == t[i%10]:
            score[2] += 1
    
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)    
    
    return answer