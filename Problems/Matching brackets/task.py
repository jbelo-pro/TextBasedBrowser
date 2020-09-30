from collections import deque
bra = input()
my_stack = deque()

for c in bra:
    if c == '(':
        my_stack.append('(')
    if c == ')':
        if len(my_stack) == 0:
            print('ERROR')
            break
        else:
            my_stack.pop()
else:
    if len(my_stack) == 0:
        print('OK')
    else:
        print('ERROR')
