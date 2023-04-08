import math
# n, k = 110011, 10
n, k = 437674, 3

# ---- 230407  10진법 소수 확인 함수 추가 ---- #
def checkPrime(num):
    if num == 1 or num == 0:
        return False
    # elif num == 2:
    #     return True
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
# ---- 만약 숫자가 엄청 큰 소수라면 시간 오래 걸릴 듯 ----


# print(checkPrime(11))
# print(checkPrime(10))
"""
def changeNumSys(n, k):
    # print(n, k)
    kSys = []
    # print('noloop')
    while True:
        # print('check')
        quotient = n//k
        remainder = int(n%k)
        # print(quotient, remainder)

        if quotient < k:
            kSys.insert(0, remainder)
            kSys.insert(0, quotient)
            break
        kSys.insert(0, remainder)
        n = quotient

    return kSys

# 테스트 케이스
n, k = n, k = 437664, 3
n, k = n, k = 437, 2
# print(changeNumSys(n, k))

# ---- ValueError: invalid literal for int() with base 10: ''  ----
# def splitNum(arr):
#     primeNum = []
#     tempNum = ''
#     for num in arr:
#         if num == 0:
#             # print('tempNum = ', tempNum)
#             if checkPrime(int(float(tempNum))) and (tempNum not in primeNum):
#                 primeNum.append(tempNum)
#                 #ValueError: invalid literal for int() with base 10: ''
#             tempNum = ''
#         else:
#             tempNum += str(num)
#         # print(tempNum, primeNum)
#     primeNum.append(tempNum)
#     return primeNum

def splitNum(arr):
    primeNum = []
    tempNum = 0
    for num in arr:
        print('num : ', num, 'temp : ', tempNum)
        if num == 0:
            if checkPrime(tempNum) :
                print("check and add")
                primeNum.append(tempNum)
            tempNum = 0
        else:
            print('tempNum B = ', tempNum)
            tempNum *= 10 
            tempNum += num 
            print('tempNum A = ', tempNum)
        print(tempNum, primeNum)
        print('----------------')
    if checkPrime(tempNum):
        primeNum.append(tempNum)
    return primeNum

def solution(n, k):
    kSys = changeNumSys(n, k)
    print('kSys : ', kSys)
    primes = splitNum(kSys)
    print('primeNum : ', primes)
    return len(primes)
"""

# ---- 함수 합치기 230408 ----

def solution(n, k):
    temp, i = 0, 1
    primes = []

    while True:
        quotient = n//k
        remainder = int(n%k)
        # quotient, remainder = divmod(n, k)

        if remainder == 0 :
            if checkPrime(temp):
                primes.append(temp)
                # print('primes : ', primes)
            temp, i = 0, 1
        else:     
            temp += remainder * i
            i *= 10

        # print('q & r : ', quotient, remainder)
        # print('T & i : ',temp, i)
        # print('------------------')
        
        n = quotient
        if quotient < k:
            temp += quotient * i
            # print(temp)
            if checkPrime(temp):
                primes.append(temp)
                # print('primes L : ', primes)
            break

    # print(primes)
    return len(primes)



# kSys = changeNumSys(n, k)
# primes = splitNum(kSys)
answer = solution(n, k)
# print('kSys : ', kSys)
# print('primeNum : ', primes)
print(answer)

