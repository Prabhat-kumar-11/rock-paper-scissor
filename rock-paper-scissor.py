import random

player_wins = 0
computer_wins = 0

def determine_winner(player_choice, computer_choice):
    global player_wins, computer_wins

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        player_wins += 1
        return "You win!"
    else:
        computer_wins += 1
        return "Computer wins!"

def get_player_choice():
    choices = ['rock', 'paper', 'scissors']
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice = int(input("Enter your choice (1-4): ")) - 1

    if player_choice == 3:
        return None
    elif player_choice < 0 or player_choice >= 3:
        print("Invalid choice. Please try again.")
        return get_player_choice()

    return choices[player_choice]

def play_round():
    player_choice_text = get_player_choice()

    if player_choice_text is None:
        return False

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("You chose:", player_choice_text)
    print("Computer chose:", computer_choice)

    result = determine_winner(player_choice_text, computer_choice)
    print(result)
    print("Player wins:", player_wins)
    print("Computer wins:", computer_wins)

    return True

def main():
    print("Welcome to Stone, Paper, Scissors!")

    while True:
        if not play_round():
            print("You have successfully quit the game")
            break

if __name__ == "__main__":
    main()
