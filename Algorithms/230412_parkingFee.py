def calTime(T_in, T_out):
    # "HH:MM"
    in_HHMM = T_in.split(':') 
    out_HHMM = T_out.split(':') 
    # print(in_HHMM, out_HHMM)
    diff_HH = int(out_HHMM[0])-int(in_HHMM[0])
    diff_MM = int(out_HHMM[1])-int(in_HHMM[1])
    return 60 * diff_HH + diff_MM

# T_in, T_out = "10:30", "11:36"
# print(calTime(T_in, T_out)

def solution(fees, records):
    [T_basic, Fee_basic, T_unit, Fee_unit] = fees
    # print(f"기본시간은 {T_basic}.")
    # print("기본 요금은 {0}.".format(Fee_basic))

    info = {}
    for record in records:
        record = record.split(" ")
        print(f'{record}')
        car_number = record[1]
        # info[car_number] = ["T_in", "T_out", "calTime", "Fee"]
        # default = ["T_in", "T_out", "calTime", "Fee"]
        # info[car_number] = default
        info[car_number] = []
        # T_in, T_out, time, fee = default    # 이거 순서!!!
        if record[2] == "IN":
            info[car_number] = [record[0]]
            T_in = info[car_number][0]
            print(info[car_number])
        elif record[2] == "OUT":
            print(type(info[car_number]))
            info[car_number].append(record[0])    # list에 append를 했는데 추가가 아니라 바뀌네...
            # info[car_number].insert(-1, record[0])    # 이래도 안됨...
            # T_out = info[car_number][1]
            print(info[car_number])
            # print("In at {T_in}, Out at {T_out}".format(T_in, T_out))
            # time = calTime(T_in, T_out)
            # info[car_number].append(time)
        print('--------------')
    print(info)


    answer = []
    return answer

# 출력 : 차량번호가 작은 차의 주차요금부터 리스트
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))