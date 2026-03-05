# A. Handmaid
name = input()
# Change the initial character of name to lowercase and prepend 'Of'.
"""
In this question, the first character of string S is an uppercase English letter, 
and all subsequent characters are lowercase English letters. 
Therefore, there is no need to specify an index when using the lower() method.
'Of' + name.lower() is enough for the answer.
"""
new_name = 'Of' + name[0].lower() + name[1:]
print(new_name)
