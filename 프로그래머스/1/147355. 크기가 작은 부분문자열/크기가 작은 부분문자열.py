def solution(t, p):
    sub_strs = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    return len([x for x in sub_strs if x <= int(p)])