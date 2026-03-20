def solution(n, lost, reserve):
    # 1. 중복 제거
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    real_lost = lost_set - reserve_set
    real_reserve = reserve_set - lost_set

    # 2. 번호 순서대로 정렬
    real_lost = sorted(real_lost)
    real_reserve = sorted(real_reserve)

    # 3. 체육복 빌려주기
    for r in real_reserve:
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)

    # 4. 수업 들을 수 있는 학생 수
    return n - len(real_lost)