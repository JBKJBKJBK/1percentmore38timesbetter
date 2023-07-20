# 230720
# def makeOrder(listSample):
#     return listSample.sort()

# listSample = [3, 4, 2, 6, 8]
# sortSample = listSample.sort()
# print(sorted(listSample, reverse=True))

def solution(n, works):
    # answer = 0

    while n > 0:    # 뭔가 더 깔끔하게 정리할 수 있을 듯 한데...
        print(f'----{n}----')
        M = max(works)

        if M == 0:
            return 0
        
        works = sorted(works, reverse = True)
        for i in range(len(works)):
            if works[i] == M and n > 0:
                works[i] -= 1
                n -= 1
            elif n <= 0:
                break
            else:
                continue
            # print(f'here! {n}  {works}')

        """
        M = max(works)
        num_M = works.count(M)
        print(f'Max and # of Max numbers : {M} & {num_M}')

        # if n >= num_M:
        n -= num_M
        works = [num-1 if num == M else num for num in works]
        print(works)
        # else:
        #     works = [works[i]-1 if works[i] == M else num]
        """

    # list comprehension 변경 >> still 시간 초과
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

# test
n = 4
works = [9, 1, 3]
print(solution(n, works))