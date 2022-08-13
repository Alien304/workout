def Palin():
    palindrom = input("Proszę podać słowo, aby sprawdzić czy jest palindromem: ")
    if palindrom == palindrom[::-1]:
        print("Palindrom")
    else:
        print("Not palindrom")

Palin()