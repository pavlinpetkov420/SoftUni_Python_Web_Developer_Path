from collections import deque


def dispenser_simulation():
    water_amount = int(input())
    people_queue = deque()

    START_COMMAND = "Start"
    END_COMMAND = "End"
    REFILL_COMMAND = "refill"

    while True:
        cmd = input()
        if cmd == START_COMMAND:
            while True:
                cmd = input()
                if cmd == END_COMMAND:
                    print(f"{water_amount} liters left")
                elif cmd.startswith(REFILL_COMMAND):
                    tokens = cmd.split()
                    liters = int(tokens[1])
                    water_amount += liters
                else:
                    liters = int(cmd)
                    if water_amount >= liters:
                        print(f"{people_queue.popleft()} got water")
                        water_amount -= liters
                    else:
                        print(f"{people_queue.popleft()} must wait")
        else:
            people_queue.append(cmd)



dispenser_simulation()