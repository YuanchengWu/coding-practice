# Complete the migratoryBirds function below.
# O(n)
def migratoryBirds(arr):
    count = {}
    current_most_common = (arr[0], 1)
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if current_most_common[1] < count[i] or (current_most_common[1] == count[i] and i < current_most_common[0]):
            current_most_common = (i, count[i])
    return current_most_common[0]

arr = [1, 5, 5, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))