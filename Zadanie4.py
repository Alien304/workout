def divisorask():
    divisor = int(input("Proszę podać numer: "))
    x = range(0, 100)
    lista = []
    for element in x:
        if element % divisor is 0:
            lista.append(element)        
    print(lista)
divisorask()