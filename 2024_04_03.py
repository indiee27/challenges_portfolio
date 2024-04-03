# challenge 1: write a function that takes an array of words and smashes them together into a sentence

def smash(words):
    sentence = ""
    for n in range(len(words)):
        sentence = sentence + words[n] + ' '
    sentence = sentence[:-1]
    return sentence

# OR tidier answer:
def smash(words):
    return " ".join(words)

print(smash(['hello', 'world']))

# challenge 2: basic calculator
def calculator(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    else:
        result = ""
    return result

# OR tidier answer

def calculator(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

print(calculator('+', 4, 7))

# challenge 3: pancake timer!

def cook_pancakes(n, m):
    from math import ceil
    if n < m:
        return 2
    else:
        return ceil((n*2)/m)