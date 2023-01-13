n, k = 437674, 3

def changeNumSys(n, k):
    # print(n, k)
    kSys = []
    print('noloop')
    i = 0
    while True:
        print('check')
        quotient = n//k
        remainder = int(n%k)
        print(quotient, remainder)
        i += 1
        if quotient < k:
            kSys.insert(0, quotient)
            break
        kSys.insert(0, remainder)
        n = quotient

    return kSys

print(changeNumSys(n, k))