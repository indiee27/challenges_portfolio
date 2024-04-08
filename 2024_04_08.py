# challenge 1: remove first and last values of a string

def remove_char(s):
    return s[1:-1]

print(remove_char('eloquent'))

# challenge 2: sum all array except the largest and smallest element

def sum_array(arr):
    if arr and len(arr)>1:
        return sum(arr) - min(arr) - max(arr)
    else:
        return 0

print(sum_array([6,2,1,8,10]))

# challenge 3: make two functions that take a list of integers and return the largest and smallest elements:

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# challenge 4:

def grow(arr):
    product = 1
    for num in arr:
        product *= num
    return product

print(grow([1, 2, 3]))