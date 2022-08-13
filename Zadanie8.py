from operator import truediv


def rockpaperscisors():
    while True:
        player1 = str.lower(input("P1 Please choose your weapon (rock, paper, scissors): "))
        player2 = str.lower(input("P2 Please choose your weapon (rock, paper, scissors): "))
        possib = ["rock", "paper", "scissors"]
        if player1 in possib and player2 in possib:
            if player1 == "rock" and player2 == "scissors":
                print("P1 has won, P2 has lost")
            elif player1 == "rock" and player2 == "paper":
                print("P1 has lost, P2 has won")
            elif player1 == "paper" and player2 == "rock":
                print("P1 has won, P2 has lost")
            elif player1 == "paper" and player2 == "scissors":
                print("P1 has lost, P2 has won")
            elif player1 == "scissors" and player2 == "paper":
                print("P1 has won, P2 has lost")
            elif player1 == "scissors" and player2 == "rock":
                print("P1 has lost, P2 has won")                                                       
            else:
                print("Draw!")
        else:
            print("Don't do it!")
            break
        answer = str.lower(input("Do you wanna play again? (yes/no) "))
        while answer == "no":
            print("Nara")
            return False
        else:
            print("Gramy dalej")
rockpaperscisors()