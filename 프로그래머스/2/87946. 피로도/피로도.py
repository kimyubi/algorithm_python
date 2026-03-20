from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for d in permutations(dungeons, len(dungeons)):
        hp, cnt = k, 0
        # 던전 탐험
        for min_required_hp, consumption in d:
            if min_required_hp <= hp:
                cnt += 1
                hp -= consumption
            else:
                break
        answer = max(answer, cnt)
    return answer