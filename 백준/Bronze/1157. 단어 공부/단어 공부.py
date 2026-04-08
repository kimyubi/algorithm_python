from collections import Counter

word = input().upper()
counter = Counter(word)
top_two = counter.most_common(2)

if len(top_two) == 1 or top_two[0][1] > top_two[1][1]:
    print(top_two[0][0])
else:
    print('?')