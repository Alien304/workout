
from typing import Type
from unittest.util import strclass


def zapytanie():
    PodajImie = input("Proszę podać swoje imię: ")
    PodajWiek = input("Proszę podać swój wiek: ")
    
    # try:
    #     PodajImie = str(PodajImie)
    #     PodajWiek = int(PodajWiek)    
    # except TypeError:
    #     print("Chuju.")
        
    Kalkulacja =(100 - int(PodajWiek))    
    
    print("Twoje imię: ", str(PodajImie), "\n", "Twój wiek: ", int(PodajWiek))
    
    if int(PodajWiek) < 100:
        print("W ciągu ", Kalkulacja, " osiągniesz wiek 100 lat." )
    elif int(PodajWiek) == 100:
        print("Łajzo próbujesz mnie oszukać?")
    else:
        print("Wypierdalaj żartownisiu!")
    
zapytanie()