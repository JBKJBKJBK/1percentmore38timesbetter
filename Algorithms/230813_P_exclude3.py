def include3(n):
    d = 10
    count = 0
    
    while n > 0:
        # print(n, n//d, n%d)
        if n%d == 3:
            return True

        n = n//d
    return False

def divide3(n):
    if n%3 == 0:
        return True
    return False


# n = 203
# n = 20300
# n = 5025
# n = 3606987059
# print(include3(n))
"""
def solution(n):
    additional = 0
    
    for i in range(1, n+1):
        if i%3 == 0:
            print(f'{i} is divided by 3')
            additional += 1
        elif include3(i) :
            print(f'{i} has letter 3')
            additional += 1
        
        print(f'{i} additional is {additional} and the answer{i + additional}')
    return n + additional
"""

def solution(n):
    if n == 10:
        return 16
    
    testNum = solution(n-1) + 1
    print(f'n is {n} testNum {testNum}')
    print(divide3(testNum) or include3(testNum))

    additional = 0
    if divide3(testNum) or include3(testNum):
        additional += 1
    
    print(f'additional {additional}')
    return testNum + additional

n = 6
n = 11
n = 13
n = 15
print(solution(n))