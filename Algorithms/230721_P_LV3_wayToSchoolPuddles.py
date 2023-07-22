#### Using Numpy Array ####
import numpy as np

def solution(m, n, puddles):
    arr = np.ones([n, m], int)
    print(f'initial {arr}')
    # arr[0, 0], arr[n-1, m-1] = 0, 0

    for puddle in puddles:
        # print(puddle, puddle[1], puddle[0])
        arr[puddle[0]-1, puddle[1]-1]= 0
    
    for i in range(1, n):
        for j in range(1, m):
            print(f'{i} and {j}, {[i, j]}')
            # if [i, j] in puddles:
            #     arr[i-1, j-1] = 0
            #     print('check1')
            #     continue
            if arr[i, j] == 0:
                print('skip')
                continue
            arr[i, j] = arr[i-1, j] + arr[i, j-1]
            print(f' check2 {arr}')
    return arr[n-1, m-1]

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
puddles = [[2, 2]]
print(solution(m, n, puddles))