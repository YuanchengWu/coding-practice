# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
import time

def urlify(s, n):
    return '%20'.join(s.split())

s = input('Enter string to urlify: ')
n = len(s)
timer = time.process_time()
print(urlify(s, n))
print(timer)