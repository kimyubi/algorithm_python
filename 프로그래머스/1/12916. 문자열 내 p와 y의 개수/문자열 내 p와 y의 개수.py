from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return True if (not c['y'] and not c['p']) or (c['y'] == c['p'])  else False