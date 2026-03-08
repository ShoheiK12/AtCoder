# AtCoder Beginner Contest 447

# A. Seats 2
"""
How to round up using //? -> rounding toward minus infinity
-> In case 3 // 2 , the answer is 1 because when the fractional part of 1.5 is removed, the nearest integer value (1) is returned.
In other words, when dealing with negative numbers, decreasing the number means increasing its absolute value. 
-> Therefore, if we truncate the decimal part of -3/2 (which is -1.5), the result we get is -2.
"""

N, M = map(int, input().split())
if M <= -(- N // 2):
    print('Yes')
else:
    print('No')

# B. mpp
"""
1. Count the occurrences of each character in sentence, recording the frequency of each character.
2. Find the max frequency among all characters.
3. Identify all characters whose frequency is equal to this max value.
4. Iterate through this sentence again from left to right.
5. If a character's frequency is the max, exclude it. Otherwise, keep the character.
6. Concatenate all the kept characters in their original order. If the resulting string is empty, output " ".
"""

sentence = input()

# 1. Count the occurrences -> Make empty dict and then check one by one. If already exist, +1.
word_count_dict = {}
for word in sentence:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# 2. Find the max -> use max() and dict.values()
max_value = max(word_count_dict.values())
# 3. Identify the max characters -> dict.items(): Iterate through the dictionary, extracting its contents as (key, value) pairs.
# -> Put key,values in k and v. -> Collect all keys that meet the conditions (if v == max_value) and return them as a list. 
key = [k for k, v in word_count_dict.items() if v == max_value]
# 4. Iterate sentence 5. Exclude of keep 6. Concatenate -> Make empty string, and then iterate sentence. 
# -> If the character is not already in the "list of characters with the max frequency," add it.
answer_sentence = ""
for char in sentence:
    if char not in key:
      answer_sentence += char
# Result
if answer_sentence == "":
    print("")
else:
    print(answer_sentence)

# C. Insert and Erase A
"""
In this question, The only insertion and deletion of 'A's can be allowed,
which means that any other characters other than A cannot be added, deleted, or rearranged.
1. Consider the impossible conditions, which means when excluding A, new_S != new_T -> Completely not matched. 
2. If the parts excluding 'A's match, then all we need to do is insert missing 'A's or delete extra 'A's. 
Therefore, the number of operations required depends only on the difference in the count of 'A's between S and T.
"""
S = input()
T = input()

# Make new sentences without A
new_S = S.replace("A", "")
new_T = T.replace("A", "")
# if new_s != new_t -> -1
if new_S != new_T:
    print("-1")
else:
    # Between S and T, how many A's can be used without modification?
    # i, j: index
    i = 0
    j = 0
    used_A = 0
    # Look through S and T from left to right
    while i < len(S) and j < len(T):
        # if S[i] == T[j], keep going
        if S[i] == T[j]:
            if S[i] == "A":
                used_A += 1
            i += 1
            j += 1
        # If find A in S, skip -> This A should be deleted
        elif S[i] == "A":
            i += 1
        # If find A in T, move forward on T side -> New A should be added
        else:
            j += 1
    # Count how many A in S and T
    aS = S.count("A")
    aT = T.count("A")
    # aS - used_A -> any A in S that were unusable need to be deleted.
    # + (aT - used-A) -> the A in T that could not be repurposed from S must be inserted.
    result = (aS - used_A) + (aT - used_A)
    print(result)

# D. Take ABC 2
"""
How to solve?
The order of deleting words must be A->B->C.
A, B and C must be deleted in the same operation.
=> How many ABC can be made?
1. Look through sentence from left to right.
2. If find A, a_count += 1. Then, go to find B.
3. If find B, a_count -= 1 and b_count += 1. Then, go to find C.
4. If find C, b_count -= 1 and answer += 1.
* While-loop is not good in this case, because every time O(n) search and O(n) delete. (Total O(n^2))
* When using for-loop, only O(n), because looking through sentence is only once.
* a_count and b_count must be -1 later, because each A,B and C can be used only once when making ABC order. 
"""
S = input()

a_count = 0
b_count = 0
answer = 0

for char in S:
    if char == "A":
        a_count += 1
    elif char == "B":
        if a_count > 0:
            a_count -= 1
            b_count += 1
    elif char == "C":
        if b_count > 0:
            b_count -= 1
            answer += 1
print(answer)

