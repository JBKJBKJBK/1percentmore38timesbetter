def checkEmpty(list):
    if len(list) > 0:
        return [max(list), min(list)]
    return [0,0]

def solution(operations):
    answer = []
    for step in operations:
        if step == "D 1" and len(answer) > 0:
            answer.remove(max(answer))
        elif step == "D -1" and len(answer) > 0:
            answer.remove(min(answer))
        elif step[0] == "I":
            stepList = step.split(' ')
            # print(stepList)
            answer.append(int(stepList[1]))  # int 추가
            # print(answer)
        # print(f'answer {answer}')    
        
    return checkEmpty(answer)

operations1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(operations1))