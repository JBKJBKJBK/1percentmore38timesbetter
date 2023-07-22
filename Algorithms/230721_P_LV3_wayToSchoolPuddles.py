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


m, n = 4, 3
puddles = [[2, 2], [2, 3]]
print(solution(m, n, puddles))