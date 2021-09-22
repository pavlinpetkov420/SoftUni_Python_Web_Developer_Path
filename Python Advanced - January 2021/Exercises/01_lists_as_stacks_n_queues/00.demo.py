# TODO FIND INFORMATION ABOUT BASIC SEARCH ALGORITHMS
#
#
# from collections import deque
#
# # n = deque(int(x) for x in input().split())
#
# n = deque()
#
# for i in range(8):
#     n.append(i)
#
# while n:
#     print(n.popleft())

from datetime import datetime

time = datetime.strptime(input(), '%H:%M:%S')
print(time)
