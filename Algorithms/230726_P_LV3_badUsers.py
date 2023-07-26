import math

def compareTwoWords(user_id, banned):
    
    for i in range(len(user_id)):
        if banned[i] == '*':
            continue
        if user_id[i] != banned[i]:
            return False
        
    return True

def findNominee(userList, banned_id):
    # input = ["frodo", "fradi", "crodo", "abc123", "frodoc"], "fr*d*"
    # output = [frodo", "fradi"]
    result = []
    
    for id in userList:
        if len(id) != len(banned_id):
            continue
        elif compareTwoWords(id, banned_id):
            result.append(id)
    return result

def solution(user_id, banned_id):
    # test previous functions
    # print(findNominee(["frodo", "fradi", "crodo", "abc123", "frodoc"], "fr*d*"))
    # >> 	['frodo', 'fradi']
    
    # case = {"fr*d*" : ["frodo", "fradi"], "abc1**" : []}
    case = {}
    
    for id in banned_id:
        # case[id] = findNominee(user_id, id)
        # print(case)    #	{'fr*d*': ['frodo', 'fradi'], 'abc1**': ['abc123']}
        case[id] = len(findNominee(user_id, id))
        print(case)    #	{'fr*d*': ['frodo', 'fradi'], 'abc1**': ['abc123']}
    answer = list(case.values())
            
        
    return math.prod(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))