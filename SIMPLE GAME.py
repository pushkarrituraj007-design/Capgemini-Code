import random


def play_stone_paper_scissors():   # --- Functionality for Game 1: Stone-Paper-Scissors ---
    choices = ["stone", "paper", "scissors"]
    user_choice = input("Enter Stone, Paper, or Scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice!")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        if (user_choice == "stone" and computer_choice == "scissors"):
            if (user_choice == "paper" and computer_choice == "stone"):
               if (user_choice == "scissors" and computer_choice == "paper"):
                    print("You win this round!")
    else:
        print("Computer wins this round!")

                        
def play_dice_roll():              # --- Functionality for Game 2: Dice Roll ---
    print("Rolling the dice...")
    player_die = random.randint(1, 6)
    computer_die = random.randint(1, 6)
    print(f"You rolled: {player_die}")
    print(f"Computer rolled: {computer_die}")

    if player_die > computer_die:
        print("You win this round!")
    elif player_die < computer_die:
        print("Computer wins this round!")
    else:
        print("It's a tie!")


def main_menu():                     # --- Menu Driven System ---
    while True:
        print("\n--- Simple Game Menu ---")
        print("1. Stone-Paper-Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            play_stone_paper_scissors()
        elif choice == '2':
            play_dice_roll()
        elif choice == '3':
            print("Exit...Thanks for playing.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
