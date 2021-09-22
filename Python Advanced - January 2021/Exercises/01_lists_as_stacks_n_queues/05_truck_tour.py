from collections import deque

stations_count = int(input())

stations_data = deque([])

for station in range(stations_count):
    stations_data.append([el for el in input().split()])

is_valid = True
tank_petrol = 0

for big_circle in range(stations_count):
    is_valid = True
    tank_petrol = 0
    for small_circle in range(stations_count):
        tank_petrol += int(stations_data[small_circle][0]) - int(stations_data[small_circle][1])

        if tank_petrol < 0:
            is_valid = False
            stations_data.append(stations_data.popleft())
            break
    if is_valid:
        print(big_circle)
        break
