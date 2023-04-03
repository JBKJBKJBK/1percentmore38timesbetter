# def numChallengers(N, stages):
#     notPassed = {}
#     challengers = {1:len(stages)}
#     failures = {}
#     for i in range(N+1):
#         notPassed[i+1] = 0
#     for stage in stages:
#         notPassed[stage] += 1
#     for i in range(1, N+1):
#         challengers[i+1] = challengers[i] - notPassed[i]
#         failures[i] = notPassed[i] / challengers[i]

#     answer = []
#     while True:
#         if len(failures) < 1:
#             break
#         maxVal = max(failures,key=failures.get) 
#         answer.append(maxVal)
#         del failures[maxVal]
    
#     return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# numChallengers(N, stages)

#----- 런타임 에러 -----------------------------


def solution(N, stages):
    notPassed = {}
    challengers = {1:len(stages)}
    failures = {}
    for i in range(1, N+1):
        notPassed[i] = stages.count(i)
        # print(notPassed)
    # for stage in stages:
    #     notPassed[stage] += 1
    for i in range(1, N+1):
        challengers[i+1] = challengers[i] - notPassed[i]
        failures[i] = notPassed[i] / challengers[i]

    answer = []
    while True:
        if len(failures) < 1:
            break
        maxVal = max(failures,key=failures.get) 
        answer.append(maxVal)
        del failures[maxVal]
    
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))