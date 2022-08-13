
def multiplenumbers():
    num = int(input("Please give number: "))
    check =  int(input("Please give a second number to check if it divides into first one: "))
    if num % check is 0:
        print("gówno")
    else:
        print("jajco")

def oddoreven():
    number = int(input("Please write number to see if it's even or odd "))
    bumber = int(input("Please write second number to see if it's even or odd "))
    if number % 2 is 0 and number % 4 is 0:
        print (f"Number {number} is even and multiple of four")
    elif number % 2 is 0:
        print (f"Number {number} is even")
    else:
        print (f"Number {number} is odd")
    
multiplenumbers()
