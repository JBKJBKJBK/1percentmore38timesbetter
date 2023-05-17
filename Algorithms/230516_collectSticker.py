# def indexDict(sticker):
#     resultDict = {}
#     for i in range(len(sticker)):
#         resultDict[i] = sticker[i]
#     return resultDict
        
# def takeMaximum(toDict):
#     values = list(toDict.values())
# 계속 변환해줘야할 듯.
# 양 옆 0으로 바꾸자

import operator
import copy

def step(sticker):
    temp = copy.deepcopy(sticker)    # 오호 deepcopy
    result = 0
    
    while sum(temp) > 0:
        maxi = max(temp)
        print(f'maximum number is {maxi}')
        result += maxi
        idx = operator.indexOf(temp, maxi)
        print(f'index of maxi is {idx}')
        temp[idx], temp[idx-1]= 0, 0
        if idx < len(sticker)-1:
            temp[idx+1] = 0
        print(f'temp is {temp}, original is {sticker}')
        print(f'------{result}------')
    return result
    
def solution(sticker):
    excluded = 0
    answer = 0
    
    while excluded < sum(sticker):
        tempSticker = sticker
        result = step(tempSticker)
        print(f'result {result}')
        if answer < result :
            answer = result 
        print(f'answer {answer}')
    
        idx = operator.indexOf(sticker, max(sticker))
        excluded += max(sticker)
        sticker[idx] = 0
        print(f'sticker!!! {sticker}')

    return answer


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))