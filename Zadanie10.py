import random

def ex10():
    a = random.sample(range(100), 10)
    b = random.sample(range(120), 15)
    customlist = [c and d for c in a for d in b if c == d != 0]
    print(a)
    print(b)
    print(customlist)
    
ex10()    
