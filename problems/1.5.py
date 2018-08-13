# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(original, edit):
    i = j = edits = 0
    o_len = len(original)
    e_len = len(edit)
    if abs(o_len - e_len) > 1:
        return False
    while i < o_len:
        if original[i] != edit[j]:
            # possible replacement
            if o_len == e_len:
                j += 1
                i += 1
            # possible insert
            elif o_len < e_len:
                j += 1
            # possible removal
            else:
                i += 1
            edits += 1
        else:
            i += 1
            j += 1
    # insert at end
    if o_len < e_len and edits == 0:
        edits += 1
    return edits == 1


original = input('Original: ')
edit = input('Edit: ')
print(one_away(original, edit))