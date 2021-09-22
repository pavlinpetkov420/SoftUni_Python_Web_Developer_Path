from collections import deque
from datetime import datetime


def deque_test():
    q = deque()

    for i in range(1 << 10):
        q.append(i)

    while q:
        x = q.popleft()


def list_queue_test():
    s = []
    for i in range(1 << 10):
        s.append(i)

    while s:
        x = s.pop()


def measure(action):
    start_time = datetime.now()
    action()
    end_time = datetime.now()
    print(f"Finished in {end_time - start_time}")


print("Dequeue:")
measure(deque_test)
print("Stack:")
measure(list_queue_test)

# TODO NEEDS FIX :)
