from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    truck = 0
    current_weight = 0
    
    # 대기 트럭이 있거나, 대기 트럭이 없더라도 다리를 아직 지나고 있는 트럭들이 있을 때 
    while truck_weights or current_weight:
        answer += 1
        # 다리에 있는 트럭 지나가게 함
        x = bridge.popleft()  
        current_weight -= x
        
        # 다리에 올라갈 트럭 + 현재 다리에 있는 트럭 무게의 합이 weight이하라면 진행시켜~
        if truck_weights:
            if truck_weights[0] + current_weight <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)   
    
    return answer