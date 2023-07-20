# 230720
def solution(n, works):
    answer = 0
    
    while n > 0:
        n -= 1
        if max(works) == 0:
            return 0

        idx = works.index(max(works))
        # print(idx)
        works[idx] -= 1
        # print(works)

    # 변경 >> still 시간 초과
    answer = sum([num**2 for num in works])
    
    return answer
        
""" 230605  >> 시간 초과
def solution(n, works):
    answer = 0
    
    while n > 0:
        n -= 1
        # print(max(works))
        if max(works) == 0:
            return 0
        idx = works.index(max(works))
        # print(idx)
        works[idx] -= 1
        # print(works)
        
    
    for num in works:
        answer += num**2
    return answer
"""

n = 4
works = [4, 3, 3]
print(solution(n, works))