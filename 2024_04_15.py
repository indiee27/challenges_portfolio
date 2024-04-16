# challenge 1: convert a number to a string
def string_to_number(s):
    return eval(s)

print(string_to_number('-134'))

# challenge 2: tribonnaci!

def tribbonaci(signature, n):
    # signature will contain 3 number, n is how many numbers are in the sequence
    count = 0
    nlist = [0] * n
    if n == 0:
        nlist = []
    else:
        [n1, n2, n3] = signature
        while count < n:
            nlist[count] = n1
            nth = n1 + n2 + n3 
            n1 = n2
            n2 = n3
            n3 = nth
            count += 1
    return nlist 

print(tribbonaci([0, 0, 1], 10))