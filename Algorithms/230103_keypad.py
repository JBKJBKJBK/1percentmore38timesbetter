numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'right'

def distance(prev, current):
    distance_x = location(prev)[0]-location(current)[0]
    distance_y = location(prev)[1]-location(current)[1]
    return abs(distance_x) + abs(distance_y)

def location(number):
    if number == 1:
        return (1, 1)
    if number == 2:
        return (1, 2)
    if number == 3:
        return (1, 3)
    if number == 4:
        return (2, 1)
    if number == 5:
        return (2, 2)
    if number == 6:
        return (2, 3)
    if number == 7:
        return (3, 1)
    if number == 8:
        return (3, 2)
    if number == 9:
        return (3, 3)
    if number == '*':
        return (4, 1)
    if number == 0:
        return (4, 2)
    if number == '#':
        return (4, 3)

def main(numbers, hand):
    result = ""
    locations = {'left' : '*', 'right' : '#'}
    # L_number = '*'
    # R_number = '#'
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            result += 'L'
            locations['left'] = number
        elif number == 3 or number == 6 or number == 9:
            result += 'R'
            locations['right'] = number
        else:
            # print('L_dist: ', distance(L_number, number))
            # print('R_dist: ', distance(R_number, number))
            if distance(locations['left'], number) < distance(locations['right'], number):
                result += 'L'
                locations['left'] = number
            elif distance(locations['left'], number) > distance(locations['right'], number):
                result += 'R'
                locations['right'] = number
            else:
                result += hand[0].upper()
                locations[hand] = number
        print(locations)


    return result

# print(distance(6, 2))
print(main(numbers, hand))
