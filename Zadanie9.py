import random
def zgaduj():
    compnum = random.randint(1, 9)
    guess = 0
    while True:
        playernum = input("Podaj numer, aby sprawdzić czy komputer wylosował tą samą liczbę: ")
        if playernum == str("exit"):
            guess = (guess + 0)
            print(f"""Wychodzisz z gry, twoja liczba prób to {guess} 
                  Komputer wybrał liczbę {compnum}""")
            return False
        # elif playernum == str(playernum):
        #     print("""Możesz wpisać liczbę, aby zgadywać lub exit, aby wyjśc z gry.
        #         Program nie zezwala na inne znaki.""")
        #     return False
        try:
            if int(playernum) == compnum:
                print(f"Gratulacje, odgałeś! Komputer wylosował {compnum}")
                guess = (guess + 1)
                print(f"Twoja liczba prób to: {guess}")
                return False
            elif int(playernum) <= compnum:
                print(f"Twoja liczba jest zbyt niska, próbuj dalej.")
                guess = (guess + 1)
            elif int(playernum) >= compnum:
                print(f"Twoja liczba jest zbyt wysoka, próbuj dalej.")
                guess = (guess + 1)
        except:
            # else:
                print("""Możesz wpisać liczbę, aby zgadywać lub exit, aby wyjśc z gry.
                    Program nie zezwala na inne znaki.""")
                return False
zgaduj()