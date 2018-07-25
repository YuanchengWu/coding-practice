# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def isUnique(s):
    if len(s) > 128:
        return False
    seen = [None] * 128
    for c in s:
        val = ord(c)
        if seen[val]:
            return False
        seen[val] = True
    return True

print(isUnique('(#@LIOV'))
