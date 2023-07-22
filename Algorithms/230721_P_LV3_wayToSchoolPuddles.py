#### Using Numpy Array ####
import numpy as np

def solution(m, n, puddles):
    arr = np.ones((n, m), np.int8)
    arr[0, 0] = 0
    # print('initial', arr)

    for puddle in puddles:
        # print(puddle)
        if len(puddle) == 0:
            break
        arr[puddle[0]-1, puddle[1]-1]= 0
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i, j] == 0:
                continue
            # RuntimeWarning: overflow encountered in scalar add
            arr[i, j] = arr[i-1, j] + arr[i, j-1]
            # print(arr)
        answer = arr[n-1, m-1]
    return int(answer)

#### Using Factorial ####
"""
import math

def calcul(horizon, vertical):
    H = math.factorial(horizon)
    V = math.factorial(vertical)
    HV = math.factorial(horizon + vertical)
    return int(HV / (H * V))
    
    
def solution(m, n, puddles):
    
    total = calcul(m-1, n-1)
    passingPuddles = 0    
    
    for puddle in puddles:
        print(puddle)
        beforePuddle = calcul(puddle[0]-1, puddle[1]-1)
        afterPuddle = calcul(m-puddle[0], n-puddle[1])
        print(beforePuddle, afterPuddle)
        passingPuddles = passingPuddles + beforePuddle * afterPuddle
        print('----', passingPuddles)
    
    return total - passingPuddles

"""



m, n = 4, 3
puddles = [[2, 2], [2, 3]]

m, n = 8, 6
puddles = [[]]
print(solution(m, n, puddles))