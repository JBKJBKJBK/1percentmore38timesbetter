def solution(d, budget):
    answer = 0
    
    d = sorted(d)
    # print(d)
    
    for one in d:
        # print(f'budget at first is {budget}')
        if budget < one:
            break
        answer += 1
        budget -= one
        
        # print(one, budget)
        
    return answer

d = [1, 3, 5, 4, 2]
budget = 9
print(solution(d, budget))