def iloscliczb():
    return int(input("Proszę podać numer ilość liczb w funkcji Fibonacciego: "))

def fibonacci():
    fib = [0, 1, 1]
    amount = iloscliczb()
    if amount == 0:
        fib = [0]
    elif amount == 1:
        fib = [0, 1]
    elif amount == 2:
        fib = [0, 1, 1]
    else:
        for amount in range(3, amount+1) :
            fib.append(fib[-1]+fib[-2])
    print(fib)
    
fibonacci()