def duration(start, end):
    start = start.split(':')
    if end == "00:00":
        end = "24:00"
    end = end.split(':')
    diffHH = int(end[0])-int(start[0])
    diffMM = int(end[1])-int(start[1])
    # print(60*diffHH + diffMM)
    return 60*diffHH + diffMM

# -------- '#' 포함된 음 고려 안 함 --------
# def playedInfo(info):
#     listInfo = info.split(',')
#     # print(listInfo)
#     time = duration(listInfo[0], listInfo[1])
    
#     L = len(listInfo[3])
#     # print(L, listInfo[3])
#     playedMelody = ""
#     for i in range(time):
#         playedMelody += listInfo[3][i%L]
#     # print(time, playedMelody, listInfo[3])
#     return listInfo[2], playedMelody

def playedInfo(info):
    listInfo = info.split(',')
    # print(listInfo)
    time = duration(listInfo[0], listInfo[1])
    
    L = len(listInfo[3])
    # print(L, listInfo[3])
    playedMelody = ""
    i = 0
    count = 0
    while count < time :
        # print(listInfo[3][i%L])
        playedMelody += listInfo[3][i%L]
        if listInfo[3][i%L] == '#':
            i += 1
            continue
        i += 1
        count += 1
    print(time, playedMelody, listInfo[3])
    return listInfo[2], playedMelody


def solution(m, musicinfos):
    answer = [0]
    # print(answer[0])
    for info in musicinfos:
        # print(playedInfo(info))
        if m in playedInfo(info)[1]:
            answer = playedInfo(info)
    if answer == [0]:
        answer = '(None)'
    return answer[0]

m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos = ["13:00,13:05,WORLD,ABCDEF", "12:00,12:14,HELLO,C#DEFGAB"]
print(solution(m, musicinfos))

