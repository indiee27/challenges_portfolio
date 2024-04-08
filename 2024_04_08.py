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