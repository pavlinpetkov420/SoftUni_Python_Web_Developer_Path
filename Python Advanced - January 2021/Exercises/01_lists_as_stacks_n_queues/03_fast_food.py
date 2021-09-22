from collections import deque
import sys

# 90/100


def orders_execution(food, orders):
    max_order = -sys.maxsize
    while orders:
        current_order = orders.popleft()
        if current_order <= food:
            food -= current_order
            if current_order > max_order:
                max_order = current_order
        else:
            orders.appendleft(current_order)
            break

    print(max_order)
    if orders:
        print("Orders left: ", end='')
        while orders:
            if len(orders) == 1:
                print(orders.pop())
                break
            print(orders.pop(), end=', ')
    else:
        print("Orders complete")


food_quantity = int(input())
orders = deque(int(x) for x in input().split())

orders_execution(food_quantity, orders)
