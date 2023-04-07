n, k = 110011, 10

def checkPrime(num):
    for i in range(2, num):
        print(i)
        if num%i == 0:
            return False
    return True

print(checkPrime(11))
print(checkPrime(10))


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
            if len(tempNum)>0 and tempNum != '1':
                primeNum.append(tempNum)
            tempNum = ''
        else:
            tempNum += str(num)
        # print(tempNum, primeNum)
    primeNum.append(tempNum)
    return primeNum

kSys = changeNumSys(n, k)
# print(kSys)
# print(splitNum(kSys))

