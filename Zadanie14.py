import random
    
olist = [random.randrange(10) for i in range(15)]
print(f"Original list: {olist}")

def looplist():
    loopers = []
    for x in olist:
        if x in loopers:
            loopers.remove(x)
        loopers.append(x)
    print(f"Loop list: {loopers}")

def setlist():
    set1 = set(olist)
    print(f"Set list: {set1}")    
                
looplist()
setlist()