def numChallengers(N, stages):
    notPassed = {}
    challengers = {1:len(stages)}
    failures = {}
    for i in range(N+1):
        notPassed[i+1] = 0
    # print(notPassed)
    for stage in stages:
        # print(stage)
        # print(notPassed[stage])
        notPassed[stage] += 1
    # print('At stage : ' , notPassed)
    for i in range(1, N+1):
        challengers[i+1] = challengers[i] - notPassed[i]
        failures[i] = notPassed[i] / challengers[i]
    # print('challengers : ' , challengers)
    # print('failures : ' , failures)

    # print(max(failures.values()))    #0.5
    # print(max(failures.keys()))    #5
    answer = []
    while True:
        if len(failures) < 1:
            break
        maxVal = max(failures,key=failures.get) 
        # 위는 한개 반환,아래는 여러개 반환
        # result = [k for k,v in failures.items() if max(failures.values()) == v]
        # print(maxVal)
        answer.append(maxVal)
        del failures[maxVal]
        # print(failures, 'answer : ', answer)
    
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
numChallengers(N, stages)
