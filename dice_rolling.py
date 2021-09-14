import random

def roll_dice(dice):
    total = 0
    for i in range(dice):
        total += random.randint(1,6)
    
    return total

def main():

    player1 = input('Who is player 1? ')
    player2 = input('Who is player 2? ')

    num_dice = int(input('How many dice will each player roll?\n'))

    player1_result = roll_dice(num_dice)
    player2_result = roll_dice(num_dice)

    print(player1, " rolled a ", player1_result, "!", sep = '')
    print(player2, " rolled a ", player2_result, "!", sep = '')

    if player1_result > player2_result:
        print(player1, "wins!")
    elif player1_result < player2_result:
        print(player2, "wins!")
    else:
        print("It's a tie!")

main()