def oneDiff(targetWord, list):
    # countNotSame = 0
    oneDifferent = []
    for word in list:
        countNotSame = 0
        for i in range(len(word)):
            # print(f'{word}, {word[i]}, {targetWord}, {countNotSame}')
            if word[i] != targetWord[i]:
                countNotSame += 1
            if countNotSame >= 2:
                continue
        if countNotSame == 1:
            oneDifferent.append(word)
        # print(f'-- {countNotSame}, {oneDifferent}')
        
    return oneDifferent
            

def solution(begin, target, words):
    if target not in words:
        return 0
    
    fromBegin = [begin]
    fromTarget = [target]
    intersection = set(fromBegin).intersection(set(fromTarget))
    
    countBegin = 0
    countTarget = 0
    
    #### begin과 target은 같지 않습니다. ####
    # if len(intersection) > 0:
    #     # print('Here is the result1')
    #     return 0
    
    while True:
        print('----start----')
        
        if countBegin + countTarget > len(words):
            return 0
        
        countBegin += 1
        for word in fromBegin:
            # words = words.remove(word)
            fromBegin = oneDiff(word, words)
            print(f'fromBegin {fromBegin}, {countBegin}')
            
            intersection = set(fromBegin).intersection(set(fromTarget))

            if len(intersection) > 0:
                # print('Here is the result2')
                return countBegin + countTarget
        
        countTarget += 1
        for word in fromTarget:
            fromTarget = oneDiff(word, words)
            print(f'fromTarget {fromTarget}, {countTarget}')
            
            intersection = set(fromBegin).intersection(set(fromTarget))

            if len(intersection) > 0:
                # print('Here is the result3')
                return countBegin + countTarget


begin, target = "hit", "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))