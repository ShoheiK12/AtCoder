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
