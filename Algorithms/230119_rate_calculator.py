#pandas로 불러오기
perimeter = [6773, 10133, 0, 11574, 26, 64, 19620, 10196, 8867, 7811, 975, 12707, 7468, 46, 14353, 10097, 8457, 4873, 10938, 7581, 17844, 12588, 10197, 8457, 9167, 12347, 8154, 11074, 11542, 7497, 6743, 14676, 10355, 16638, 7483, 5929, 14]

basic_rate = 0.01
success_rate = 0.11
total_days = 182

def count_success(perimeter):
    success = 0
    for num_steps in perimeter:
        if num_steps >= 10000:
            success += 1
    return success

current_day = len(perimeter)
print("미션 시작한 지 ", current_day, "일째 입니다.")
success_days = count_success(perimeter)
fail_days = current_day - success_days
print('미션 성공일 수는 ', success_days, '일입니다.')
print('현재까지 모은 원금은 ', round(0.0001*(10000*success_days+5000*(fail_days+1)),1), '원입니다.')

def saving_temp(num_steps, left_days):
    if num_steps >= 10000:
        return 10000*(1+success_rate*left_days/365)
    else:
        return 5000*(1+basic_rate*left_days/365)

# savings = 5000    #가입금액 5천원
def cal_savings(perimeter, total_days):
    savings = 5000    #가입금액 5천원
    for i in range(len(perimeter)):
        left_days = total_days-i
        temp = saving_temp(perimeter[i], left_days)
        savings += temp
        # print(savings, left_days)
    return savings

savings = cal_savings(perimeter, total_days)
# print(savings)

print('현재까지 모인 금액은 ', round(0.0001*savings, 1), "만원입니다.")

#지금부터 매일 만보 성공하면
perimeter_max = perimeter
while len(perimeter_max)<total_days:
    perimeter_max.append(10000)
# print(len(perimeter_max))


max_savings = cal_savings(perimeter_max, total_days)
print('앞으로 모을 수 있는 최대 금액은 ', round(0.0001*max_savings, 1), "만원입니다.")
# print(fail_days)
original_savings = 10000*(total_days-fail_days)+5000*(fail_days+1)
interest = max_savings - original_savings
print('이 경우 모은 원금은 ', round(0.0001*original_savings, 1), '만원입니다.')
print('이 경우 받을 수 있있는 이자는 ', round(0.0001*interest, 1), '만원입니다.')
