nums = "0123456789"

def separate(filename):
    Head, Number, Tail = '', '', ''
    passHead = False
    passNumber = False
    for letter in filename:
        # print(letter)
        if letter in nums:
            passHead = True
        if passHead and letter not in nums:
            passNumber = True
            
        if not passHead:
            Head += letter
        elif not passNumber:
            Number += letter
        else:
            Tail += letter

    return Head, Number, Tail

# print(separate('F-5 Freedom Fighter'))

def solution(files):
    dict_files = {}
    for file in files:
        # Head, Number, Tail = separate(file)
        dict_files[file] = separate(file)
    print(dict_files)

    answer = []
    return answer


files1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files1))
# print(solution(files2))

# ---- test ----
# print(int('F'))
# print(type('F'))