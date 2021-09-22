from collections import deque

s_queue = deque()

PAID_COMMAND = "Paid"
END_COMMAND = "End"

while True:
    cmd = input()

    if cmd == END_COMMAND:
        print(f"{len(s_queue)} people remaining.")
        break
    elif cmd == PAID_COMMAND:
        while s_queue:
            print(s_queue.popleft())
    else:
        s_queue.append(cmd)
