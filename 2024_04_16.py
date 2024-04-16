# challenge 1: greetings

def greet(name):
    return f"Hello, {name} how are you doing today?"

print(greet('indie'))

# challenge 2: get the middle character

def get_middle(s):
    if len(s) % 2 == 1:
        return s[int(len(s)/2)]
    else:
        return s[int((len(s)-1)/2)] + s[int((len(s)+1)/2)]
    
print(get_middle('string'))
