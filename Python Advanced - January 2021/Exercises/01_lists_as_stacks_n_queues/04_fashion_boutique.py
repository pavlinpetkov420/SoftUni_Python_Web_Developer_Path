box = list(map(int, input().split()))
capacity = int(input())

racks_counter, total_volume = 1, 0
current_capacity = capacity
while box:
    current_clothes_volume = box.pop()

    if current_clothes_volume <= current_capacity:
        current_capacity -= current_clothes_volume
    else:
        racks_counter += 1
        current_capacity = capacity
        current_capacity -= current_clothes_volume

print(racks_counter)

