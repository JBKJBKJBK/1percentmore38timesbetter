def solution(s):
    # print('Z'>'a') >> FALSE
    # print('A'<'a') >> TRUE
    # print('A'<'z') >> TRUE
    
    while True:
        count = 0

        for i in range(len(s)-1):
            print(s[i])
            if s[i] < s[i+1]:
                count += 1
                s[i], s[i+1] = s[i+1], s[i]
                print(s)
        if count == 0:
            break
        
    return s

s = "Zbcdefg"
print(solution(s))