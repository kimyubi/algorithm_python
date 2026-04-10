def solution(str1, str2):
    a = [str1[i:i+2].lower() for i in range(len(str1) -1) if str1[i:i+2].isalpha()]
    b = [str2[i:i+2].lower() for i in range(len(str2) -1) if str2[i:i+2].isalpha()]
    
    # 집합 a와 b가 모두 공집합일 경우에는 자카드 유사도 1
    if not a and not b:
        return 65536
    
    set_a, set_b = set(a), set(b)
    gyo = set_a & set_b
    hap = set_a | set_b
    
    # 교집합 원소 개수 구하기
    gyo_sum = sum([min(a.count(g), b.count(g)) for g in gyo])
    # 합집합 원소 개수 구하기
    hap_sum = sum([max(a.count(h), b.count(h)) for h in hap])
    
    
    # 자카드 유사도 : 교집합 크기 / 합집합 크기
    return int((gyo_sum / hap_sum) * 65536)