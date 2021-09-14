import random

def main():
    player_name = input("Greetings, imbecile. Besides \"loser,\" what should I call you? ")
    print("\nOh, goody... Another " + player_name + "\n")
    print("I'm thinking of a number between 1 and 100... Let's see how many tries it takes you to get it.\n\nWhat's your first guess?", end = ' ')
    comp_num = random.randint(1, 100)
    def take_a_guess(guesses):
        guess = int(input(' '))

        if guess == comp_num:
            print("Oh, well done, monkey. You found my number in", guesses, "guess" + ('es' if guesses > 1 else '') + '. Here\'s a banana.')
            return
        else:
            if guess > comp_num:
                print("Oh, too bad. You need to go lower, you carbon-based buffoon.")
            else:
                print("Rise from the slime, primitive creature. You should guess higher next time.")
            guesses += 1
            print("What's your next guess? ", end = '')
            take_a_guess(guesses)

    take_a_guess(1)

main()
