from collections import deque
n = int(input())

my_stack = deque()
for x in range(n):
    action = input()
    if action == 'READ' and len(my_stack) > 0:
        print(my_stack.pop())
    else:
        my_stack.append(action[action.find(' ') + 1:])
