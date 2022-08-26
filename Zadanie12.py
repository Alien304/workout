import random

def randomlist():
    return random.sample(range(0,100), 15)

def mixmaxlist():
    return [i for i in a if i == a[0] or i == a[-1]]

a = randomlist()
b = mixmaxlist()

print(a)
print(b)