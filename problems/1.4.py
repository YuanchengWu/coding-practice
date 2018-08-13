# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

def palindrome_permutation(s):
    seen = set()
    counter = 0
    for c in s:
        if c != ' ':
            if c not in seen:
                seen.add(c)
            counter += 1
    return counter % 2 == len(''.join(s.split())) % 2

s = input('Enter string: ')
print(palindrome_permutation(s))