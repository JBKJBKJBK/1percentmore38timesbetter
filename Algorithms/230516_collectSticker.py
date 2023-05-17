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

def step(sticker):
    result = 0
    
    while sum(sticker) > 0:
        maxi = max(sticker)
        print(f'maximum number is {maxi}')
        result += maxi
        idx = operator.indexOf(sticker, maxi)
        print(f'index of maxi is {idx}')
        sticker[idx], sticker[idx-1], sticker[idx+1] = 0, 0, 0 
        print(f'sticker is {sticker}')
    print('------------------')
    return result
    
def solution(sticker):
    original = sticker
    excluded = 0
    answer = 0
    print(f'excl {excluded}, sticker {original}, ans {answer}')
    
    while excluded < sum(original):
        print(f'answer {answer}')
        if answer < step(original):
            answer = step(original)
        print(f'sticker! {sticker}, original! {original}')
        idx = operator.indexOf(sticker, max(sticker))
        excluded += max(sticker)
        original[idx] = 0
        print(f'sticker!!! {sticker}, original!!! {original}')

    return answer


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))