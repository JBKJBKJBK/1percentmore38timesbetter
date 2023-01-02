cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

timeHit = 1
timeMiss = 5

time = 0
dictCities = {}
for city in cities:
    dictCities[city] = cacheSize
print(dictCities)

cacheCities = []

for city in cities:
    if city in cacheCities:
        time += timeHit
        cacheCities.remove(city)
        cacheCities.append(city)
        print('Hit: ' , cacheCities)
    else:
        time += timeMiss
        # cacheSize = 0 인 경우 pop()에러 발생
        if cacheSize == 0:
            continue  
        # 'cacheSize != 0 and' 작성 시, 29번째 줄 애매
        elif len(cacheCities) >= cacheSize:
            cacheCities.pop(0)
        cacheCities.append(city)
        print('Miss: ' , cacheCities)

print(time)
# print(cacheCities)
