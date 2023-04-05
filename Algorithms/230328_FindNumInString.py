numList = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9' ] 
numStr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = ''
    i = 1

    while i<12:    
        if len(s) == 0:
            return int(answer)
        else:
            word = s[:i]
            # print(word)
            if word in numList:
                answer += word
                s = s[i:]
                i = 1
                # print(':)', s)
                continue
            elif word in numStr:
                # print('W',word)
                num = numStr.index(word)
                # print('#', num)
                answer += str(num)
                # print('A',answer)
                s = s[i:]
                i = 1
                # print(':P', s)
                continue

        i += 1


st = 'one4seveneight'
print(solution(st))



#---------- 2023/03/28 ----------
# def solution(s):
#     answer = ""
#     if len(s) == 0:
#         return answer
    
#     if s in numStr:
#         num = numStr.index(s)
#         answer += str(num)
#         s = ""
#     elif s in numList:
#         answer += s
#         s = ""

#     for i in range(len(s)):
#         word = s[:i]
#         # print(word)
#         if word in numList:
#             answer += word
#             s = s[i:]
#             break
#         elif word in numStr:
#             print('W',word)
#             num = numStr.index(word)
#             print('#', num)
#             answer += str(num)
#             print('A',answer)
#             s = s[i:]
#             break
        
#     return int(answer)