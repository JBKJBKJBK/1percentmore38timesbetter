import string

letters = string.ascii_letters
list_pairs = [letter+letter for letter in letters]
# print(list_pairs)

def solution(s):
    # i = 0
    idx = 0

    while len(s) > 0:
        # i += 1
        # print('while', i)
        # if i == 5:
        #     break  
        
        check_pairs = s[idx]+s[idx+1]
        
        idx += 1

        if check_pairs in list_pairs:
            # s.replace(check_pairs, "")
            s_new = s.replace(check_pairs, "", 1)
            
            # if i == len(s)-1:
            #     s = s[:i]
            
            # print(s[:i], s[i+2:])
            # s = s[:i] + s[i+2:]
            # print(s)
            
            s = s_new
            idx = 0
        if len(s) == 0:
            return 1
        
        if idx >= len(s)-1:
            return 0


#### test
s1 = 'baabaa'
s2 = 'cdcd'

print(solution(s1))
print(solution(s2))

#'MiscTests'.removesuffix('Tests') >> 