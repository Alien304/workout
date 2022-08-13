from itertools import count


# def lista():
#     mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     mylist2 = []
#     for element in mylist:
#         if element > 5:
#             mylist2.append(element)
#             print (element)
def lista2():
    mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    mylist2 = []
    yournumber = int(input("Proszę podaj liczbę: "))
    for element in mylist:
        if element > yournumber:
            mylist2.append(element)
            print (element)    
    
lista2()