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


# def solution(N, stages):
#     notPassed = {}
#     challengers = {1:len(stages)}
#     failures = {}
#     for i in range(1, N+1):
#         notPassed[i] = stages.count(i)
#         # print(notPassed)
#     # for stage in stages:
#     #     notPassed[stage] += 1
#     # for i in range(1, N+1):
#         challengers[i+1] = challengers[i] - notPassed[i]
#         failures[i] = notPassed[i] / challengers[i]
#         print(failures)

#     # answer = []
#     # while True:
#     #     if len(failures) < 1:
#     #         break
#     #     maxVal = max(failures,key=failures.get) 
#     #     answer.append(maxVal)
#     #     del failures[maxVal]
#     # print(sorted(failures,key=lambda x:failures[x], reverse=True))
    
#     return sorted(failures,key=lambda x:failures[x], reverse=True)

#----- 런타임 에러 -----------------------------
# 런타임 에러는 보통 어떤 이유로든 코드를 정상 종료할 수 없을 때 납니다. 
# 정확히 모르겠지만 혹시 n 나누기 0 같은걸 하신건 아닐까요?

def solution(N, stages):
    notPassed = {}
    challengers = {1:len(stages)}
    failures = {}
    answer = []
    for i in range(1, N+1):
        notPassed[i] = stages.count(i)
        challengers[i+1] = challengers[i] - notPassed[i]       #challengers 가  0이 되는 경우
        if challengers[i] == 0:                                #challengers = notPassed
            failures[i] = 0
        else:
            failures[i] = notPassed[i] / challengers[i]            
    # print('notPassed :', notPassed)
    # print('challengers :', challengers)
    # print('failures : ', failures)

    answer = sorted(failures,key=lambda x:failures[x], reverse=True)
    return answer

N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [2, 1, 2, 2, 2, 4, 3, 3]

print(solution(N, stages))