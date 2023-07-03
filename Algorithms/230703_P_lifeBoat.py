def checkLimit(arr, new_W, limit):
    # array 안의 숫자 합이 limit 넘을 경우,
    # (못 타는 경우) True
    # (탈 수 있는 경우) False
    if sum(arr) + new_W > limit :
        return True
    
    return False

# 가장 무거운 사람 각 보트에 더했을 때
# limit 넘으면 새 보트, 안 넘으면 그 보트
def boatNumtoAdd(boat_dict, max_W, limit):
    numBoat = len(boat_dict)
    if numBoat == 0 :
        return numBoat + 1

    for i in range(numBoat):
        if not checkLimit(boat_dict[i+1], max_W, limit):
            return i+1
        
    return numBoat + 1

def solution(people, limit):
    # i = 0
    boat_dict = {}
    
    while len(people) > 0 :
    # while i < 5:
        # i += 1
        
        if len(people) <= 0 :
            break
        
        # 현재 보트 개수
        current_boat = len(boat_dict)
        print(f'The number of boats : {current_boat}')
        
        # 가장 무거운 사람의 index
        heaviest = people.index(max(people))
        print(f'The index of heaviest : {heaviest}', max(people))
        
        # 가장 무거운 사람 각 보트에 더했을 때
        # limit 넘으면 새 보트, 안 넘으면 그 보트
        newMember = boatNumtoAdd(boat_dict, max(people), limit)
        print(f'Boat number to have new member : {newMember}')
        
        if newMember <= current_boat:
            boat_dict[newMember].append(max(people))
        else:
            boat_dict[newMember] = [max(people)]
        print(f'boat status : {boat_dict}')
        people.pop(heaviest)
        print(f'----{people}----')
    
    
    return len(boat_dict)


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))