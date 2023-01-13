record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def message(list):
    if list[0] == 'Enter':
        return '`list[2]`님이 들어왔습니다.'

print(message(['Enter', 'uid1234', 'Muzi']))


def solution(record):

    record_split = []
    for info in record:
        # print(info.split(' '))
        record_split.append(info.split(' '))
    # print(record_split)

    answer = []
    
    return answer

print(solution(record))