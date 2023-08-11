import string

def alphabetDict():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    # print(alphabets)
    L = len(lower)

    numDictionary = {}
    dictionary = {}
    for i in range(L):
        numDictionary[i] = upper[i]
        numDictionary[i+L] = lower[i]

        dictionary[upper[i]] = i
        dictionary[lower[i]] = i+L

    return dictionary, numDictionary

# dictionary, numDictionary = alphabetDict()
# print(dictionary, numDictionary)

# def solution(s):
#     # print('Z'>'a') >> FALSE
#     # print('A'<'a') >> TRUE
#     # print('A'<'z') >> TRUE
#     """
#     while True:
#         count = 0

#         for i in range(len(s)-1):
#             print(s[i])
#             if s[i] < s[i+1]:
#                 count += 1
#                 s[i], s[i+1] = s[i+1], s[i]  #'str' object does not support item assignment
#                 print(s)
#         if count == 0:
#             break
#     """

#     dictionary, numDictionary = alphabetDict()
#     # print(dictionary, numDictionary)
#     numbers = []
#     for i in range(len(s)):
#         numbers.append(dictionary[s[i]])
    
#     # print(numbers)
#     numbers = sorted(numbers, reverse=True)
#     # print(numbers)
    
#     answer = ''
#     for num in numbers:
#         answer += numDictionary[num]
        
#     return answer


## 다른 사람 풀이 

def solution(s):
    return ''.join(sorted(s, reverse=True))

s = "Zbcdefg"
print(solution(s))