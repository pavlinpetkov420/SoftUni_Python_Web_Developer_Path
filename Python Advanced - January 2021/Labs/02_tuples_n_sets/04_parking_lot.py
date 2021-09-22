def input_lines(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(parking_lot):
    if parking_lot:
        for car_plate in parking_lot:
            print(car_plate)
    else:
        print("Parking Lot is Empty")


lines_count = int(input())
data = input_lines(lines_count)
parking_lot = set()

for line in data:
    command, car = line.split(', ')
    if command == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

print_result(parking_lot)