import math
# import numpy as np

# n : 전파 안 닿는 건물 수
# w : 닿는 거리
# ------+----
# 6개에 전파 보내려면 몇개 필요한지 반환
def needStation(n, w):
    cover = 2*w + 1
    return math.ceil(n/cover)

def solution(n, stations, w):
    # already = [[start, end], [start, end], ...]
    already = []
    noStation = []

    for i in range(len(stations)):
        already.append([stations[i]-w, stations[i]+w])
        print(f'already {already}')
        if i == 0: 
            gap = already[i][0] - 1
            print(f'if : {gap}')
        # elif i == len(stations)-1:
        #     gap = n - already[i][1]
        #     print(f'if + : {gap}')
        else:
            gap = already[i][0] - already[i-1][1] - 1
            print(f'else {gap}')
        
        if gap > 0:
            noStation.append(gap)

    gap = n - already[i][1]
    print(f'if + : {gap}')
    if gap > 0:
        noStation.append(gap)
    # print(f'already {already}')
    print(f'noStaion {noStation}')

    answer = 0
    for num in noStation:
        # print(needStation(num, w))
        answer += needStation(num, w)

    return answer

# -------- 230429 2차 시도 --------
""" 
# n : 전파 안 닿는 건물 수
# w : 닿는 거리
# ------+----
# 6개에 전파 보내려면 몇개 필요한지 반환
def needStation(n, w):
    cover = 2*w + 1
    return math.ceil(n/cover)

def solution(n, stations, w):
    answer = 0
    
    # already = []
    # for station in stations:
    #     already.append(station)
    #     for i in range(1, w+1):
    #         already.append(station-i)
    #         already.append(station+i)
    # print(f'already {already}')
        
    nonStations = []
    already = False
    count = 0
    for i in range(1, n+1):
        for station in stations:
            # print('here', station-w, station+w+1)
            if i in range(station-w, station+w+1):
                # print('check1')
                already = True
                # print(i, 'Lets break')
                break
            # print('break?')
        # print('check2', count)
        if not already:
            count += 1
        if already and count != 0:
            nonStations.append(count)   
            count = 0
        already = False
    # print(nonStations)
    
    for num in nonStations:
        # print(needStation(num, w))
        answer += needStation(num, w)
    
    return answer
"""
n = 11
stations = [4, 11]
w = 1

n = 16
stations = [9]
w = 2

print(solution(n, stations, w))
# print(4 in (3, 6))        #false
# print(4 in range(3, 6))   #true