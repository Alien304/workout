def numberask(help_text="Proszę podać numer: "):
    return int(input(help_text))

yournumber = numberask()
if yournumber % 2 is 0:
    print(f"Twój numer to: {yournumber} i jest parzysty")    
else:
    print(f"Twój numer to: {yournumber} i nie jest parzysty")