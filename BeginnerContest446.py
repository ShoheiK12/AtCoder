# A. Handmaid
"""
In this question, the first character of string S is an uppercase English letter, 
and all subsequent characters are lowercase English letters. 
Therefore, there is no need to specify an index when using the lower() method.
'Of' + name.lower() is enough for the answer.
"""

name = input()
# Change the initial character of name to lowercase and prepend 'Of'.
new_name = 'Of' + name[0].lower() + name[1:]
print(new_name)

# B. Greedy Draft
"""
How to solve?
1. Manage if the drink is already chosen or not.
2. Deal with customers one by one
3. Check the list
"""

# N = the number of guests, M = the number of drinks
N,M = map(int, input().split())

# Make left drink list. False = not drink yet. +1: index start with 0.
used = [False] * (M + 1)

# Deal with customers one by one using for-loop
for i in range(N):
    # Enter the length of wish_list
    L = int(input())
    wish_list = list(map(int, input().split()))

    # Initial setting is water(0)
    drink = 0

    # Check the list
    for x in wish_list:
        # If chosen drink is not used, then add this drink and change False to True(used)
        if not used[x]:
            drink = x
            used[x] = True
            break

    print(drink)

# C. Omelette Restaurant
"""
How to Solve?
1. Manage egg stock by FIFO.
2. Use the oldest eggs first.
3. If eggs still remain, calculate the egg stock
4. Throw the eggs away if they are expired
"""

from collections import deque

T = int(input())

# Simulate test one by one
for _ in range(T):
    # N = open days, D = disposal day
    N, D = map(int, input().split())
    # A = How many eggs bought, B = How many eggs used
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Manage egg stock using deque() -> (purchase day, number of eggs)
    stock = deque()

    for day in range(N):

        # How many eggs we buy
        stock.append([day, A[day]])

        # How many eggs we can use today
        use = B[day]

        while use > 0:
            # stock[0] = the oldest egg
            d, count = stock[0]

            # If count <= use, use all eggs
            if count <= use:
                use -= count
                # Delete the oldest stock
                stock.popleft()
            # Number of stock > number of eggs we want to use
            else:
                # stock[0][1] = number of eggs bought
                # stock[0] = [0,7] (purchase day, number of eggs), we cannot calculate list.
                # stock[0][1] -= use -> number of egg stock
                stock[0][1] -= use
                # use = 0 -> Today's egg demand has been met.
                use = 0

        # If we have still stock and "Today's Date" - "Purchase day" >= 0 -> Dispose of eggs
        while stock and day - stock[0][0] >= D:
            stock.popleft()

    result = 0
    # How many eggs remain
    for d, count in stock:
        result += count

    print(result)
