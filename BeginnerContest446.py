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
