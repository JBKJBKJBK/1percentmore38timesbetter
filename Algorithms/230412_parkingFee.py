import math

def calTime(T_in, T_out):
    # "HH:MM"
    in_HHMM = T_in.split(':') 
    out_HHMM = T_out.split(':') 
    diff_HH = int(out_HHMM[0])-int(in_HHMM[0])
    diff_MM = int(out_HHMM[1])-int(in_HHMM[1])
    return 60 * diff_HH + diff_MM

# T_in, T_out = "10:30", "11:36"
# print(calTime(T_in, T_out)

# ---- 230424 ----
def CalFee(time, fees):
    default = fees[1]
    additional = fees[3]

    if time <= fees[0]:
        return default
    else :
        temp = time - fees[0]
        times = math.ceil(temp/fees[2])
        return default + additional * times

fees = [180, 5000, 10, 600]
time = 670
print(CalFee(time, fees))

''''
# ---- 230425 ----
def sortAscending(dict):
    keys = list(dict.keys())
    keys.sort()
    answer = []
    for idx in range(len(keys)):
        answer.append(dict[keys[idx]])
    return answer
'''

# ---- 230425 ----
def inNouts(records):
    inNout = {}
    for record in records:
        record = record.split(" ")
        car_number = record[1]
        inNout[car_number] = []

    for record in records:
        record = record.split(" ")
        # print(f'{record}')    # ['HH:MM', '차량번호', 'IN/OUT']
        car_number = record[1]
        # print('check', inNout[car_number])    # error
        if record[2] == "IN":
            inNout[car_number].append(record[0]) 
        elif record[2] == "OUT":
            inNout[car_number].append(record[0]) 
    return inNout

# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# print(inNouts(records))

"""
def solution(fees, records):
    # info = {차량넘버 : [T_in, T_out]}
    # timeD = {차량넘버 : 누적 시간}
    # feeD = {차량넘버 : 요금}
    info, status, timeD, feeD = {}, {}, {}, {}

    # 이중 반복은 하기 싫은데...
    for record in records:
        record = record.split(" ")
        car_number = record[1]
        timeD[car_number] = 0
        feeD[car_number] = 0

    for record in records:
        record = record.split(" ")
        print(f'{record}')
        car_number = record[1]
        
        if record[2] == "IN":
            status[car_number] = 'IN'
            info[car_number] = [record[0]]

        elif record[2] == "OUT":
            status[car_number] = 'OUT'
            # print(type(info[car_number]))
            info[car_number].append(record[0])    # list에 append를 했는데 추가가 아니라 바뀌네...
            # info[car_number].insert(-1, record[0])    # 이래도 안됨...
            time = calTime(info[car_number][0], info[car_number][1])
            timeD[car_number] += time
        print('----', info)
        print(f'-------{timeD}-------')
        print(f'--{info[car_number]}--')
            # fee = CalFee(time, fees)
            # print(f'time {time} fee {fee}')
            # feeD[car_number] += fee
        # print(f'-------{feeD}-------')
    # print(info)

    return sortAscending(feeD)
"""

# ---- 230425 ----
def solution(fees, records) :
    info = inNouts(records)
    carNum = list(info.keys())
    carNum.sort()

    timeD = {}
    feeD = {}

    for num in carNum:
        timeD[num] = 0
        print(info[num])
        if len(info[num])%2 == 1:
            info[num].append('23:59')
        
        visit = int(len(info[num])/2)
        # print(visit)

        for i in range(visit):
            T_in = info[num][2*i]
            T_out = info[num][2*i+1]
            print(T_in, T_out)
            time = calTime(T_in, T_out)
            print(f'before {timeD}')
            timeD[num] += time
            print(f'after {timeD}')
        print('-------------')

        feeD[num] = CalFee(timeD[num], fees)
        print(f'Fee {feeD}')

    return list(feeD.values())

# 출력 : 차량번호가 작은 차의 주차요금부터 리스트
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# print(solution(fees, records))

'''
# ---- test : dictionary[key] ----
testDict = {}
testDict['key1'] = 'value1'
testDict['key2'] = 'value2'
testDict["key1"] = 'newValue'
print(testDict)    # {'key1': 'newValue', 'key2': 'value2'}
'''