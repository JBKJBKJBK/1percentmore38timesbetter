import string

def SplitYYMMDD(stringYYMMDD):
    # print(stringYYMMDD)
    listYYMMDD = stringYYMMDD.split('.')
    # print(listYYMMDD)
    year, month, date = int(listYYMMDD[0]), int(listYYMMDD[1]), int(listYYMMDD[2])
    return year, month, date

# print(SplitYYMMDD("2023.03.16"))

def AssembleYYMMDD(listYYMMDD):
    # string = str(listYYMMDD[0])
    if listYYMMDD[1] < 10:
        tempMM = "0" + str(listYYMMDD[1])
    else:
        tempMM = str(listYYMMDD[1])
    # print(tempMM)
    if listYYMMDD[2] < 10:
        tempDD = "0" + str(listYYMMDD[2])
    else:
        tempDD = str(listYYMMDD[2])
    # print(tempDD)
    return str(listYYMMDD[0]) + tempMM + tempDD

# print(AssembleYYMMDD([2023, 3, 27]))

def termsToDict(terms):
    termsDict = {}
    for term in terms:
        splitString = term.split(' ')
        termsDict[splitString[0]] = int(splitString[1])
    return termsDict

# print(termsToDict(["A 6", "B 12", "C 3"]))


# privacies = ["날짜 A", "날짜 B"]
#privacy = "날짜 A"
def ExpiredDate(termsDict, privacies):
    expired = [] 
    for privacy in privacies:
        separate = privacy.split(' ')
        # print(separate)
        startDate = separate[0]
        startDate = list(SplitYYMMDD(startDate))
        # print(startDate[1]+termsDict[separate[1]])
        expiredMonth = startDate[1]+termsDict[separate[1]]
        while expiredMonth > 12:
            # print(startDate[0], expiredMonth)
            startDate[0] += 1
            expiredMonth -= 12
            # print(startDate[0], expiredMonth)
        expired.append([startDate[0], expiredMonth, startDate[2]])
    return expired

today = "2022.05.19"
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
terms = ["A 6", "B 12", "C 3"]

termsDict = termsToDict(terms)
expired = ExpiredDate(termsDict, privacies)
print(expired)
result = []
for idx in range(len(expired)):
    # print(expired[idx])
    if AssembleYYMMDD(expired[idx]) > today:
        print(expired[idx])
        result.append(idx+1)
print(result)