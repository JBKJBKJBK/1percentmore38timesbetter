def skillDict(skill):
    skillDict = {}
    for i in range(len(skill)):
        skillDict[skill[i]] = i
    return skillDict
        
"""
def solution(skill, skill_trees):
    dict = skillDict(skill)
    keys = dict.keys()
    skill_order = list(range(len(skill)))
    print(dict, keys)
    # print(skill_order)
    
    answer = 0
    for skill in skill_trees:
        L = len(skill)
        
        order = []
        for i in range(L):
            # print('check')
            if skill[i] in keys:
                order.append(dict[skill[i]])
            # print(f'order 1 {order}')
        print(f'order 2 {order}')
        
        for j in range(len(order)):
            print(skill_order[j], order[j])
            if skill_order[j] != order[j]:
                break
            if j == len(order)-1:
                answer += 1
            # if order[j] < order[j-1]:
            #     print('here')
            #     break
            # if j == len(order)-1:
            #     print('answer+1')
            #     answer += 1
        print(f'----answer {answer}----')
        
    return answer
"""

def solution(skill, skill_trees):
    return

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	

print(solution(skill, skill_trees))