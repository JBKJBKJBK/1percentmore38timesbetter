cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

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
        time += 1
        cacheCities.remove(city)
        cacheCities.append(city)
        print('Hit: ' , cacheCities)
    else:
        time += 5
        if len(cacheCities) >= 3:
            cacheCities.pop(0)
        cacheCities.append(city)
        print('Miss: ' , cacheCities)

print(time)
print(cacheCities)
