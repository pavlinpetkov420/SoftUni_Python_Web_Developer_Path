from collections import deque

players = deque(input().split())
step = int(input())


while len(players) > 1:
    for _ in range(step - 1):
        players.append(players.popleft())
    print(f"Removed {players.popleft()}")

print(f"Last is {players.popleft()}")


# TODO THERE IS ONE MORE SOLUTION IN THE VIDEO!!!
