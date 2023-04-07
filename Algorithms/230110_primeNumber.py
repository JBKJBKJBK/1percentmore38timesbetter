# n, k = 110011, 10
n, k = 437674, 3

# ---- 230407  10진법 소수 확인 함수 추가 ---- #
def checkPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

# print(checkPrime(11))
# print(checkPrime(10))

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
    

def splitNum(arr):
    primeNum = []
    tempNum = ''
    for num in arr:
        if num == 0:
            print('tempNum = ', tempNum)
            if checkPrime(int(tempNum)):
                primeNum.append(tempNum)
                tempNum = ''
        else:
            tempNum += str(num)
        print(tempNum, primeNum)
    primeNum.append(tempNum)
    return set(primeNum)

kSys = changeNumSys(n, k)
print('kSys : ', kSys)
print('primeNum : ', splitNum(kSys))

