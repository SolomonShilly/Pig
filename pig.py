from random import randint

playerScore = 0
computerScore = 0

def update_score(score, dieValue):
    if dieValue == 1:
        return 0
    else:
        return score + dieValue

def display_scoreboard(playerScore, computerScore):

    print()
    print("-" * 20)
    print(f"Player Score: {playerScore}")
    print(f"Computer Score: {computerScore}")
    print("-" * 20)
    print()

welcomeMessage = """
          Welcome to 'Pig', a dice game!

    In this game, a user and a computer opponent
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""

print(welcomeMessage)
username = input("What is your name? ")

while True:
    input(f"Press 'Enter' to roll the die {username}!\n")
    playerValue = randint(1, 6)
    print(f"{username} rolls a {playerValue}")

    computerValue = randint(1, 6)
    print(f"Computer rolls a {computerValue}")

    playerScore = update_score(playerScore, playerValue)
    computerScore = update_score(computerScore, computerValue)
    display_scoreboard(playerScore, computerScore)
    if playerScore >= 30:
        print(f"{username} wins!")
        break
    elif computerScore >= 30:
        print("Computer wins!")
        break