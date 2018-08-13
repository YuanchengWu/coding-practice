# Check Permutation: Given two strings,
# write a method to decide if one is a permutation of the other.

def checkPermutation(a, b):
    if len(a) != len(b):
        return False
    return set(a) == set(b)
a = input('Enter a: ')
b = input('Enter b: ')
print(checkPermutation(a, b))