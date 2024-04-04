# challenge 1: Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers

def sum_mix(arr):
    for i in range(len(arr)):
        if type(arr[i]) == str:
            arr[i] = int(arr[i])
    return sum(arr)

# OR tider answer:
def sum_mix(arr):
    return sum(map(int, arr))

print(sum_mix([3,'4',7]))