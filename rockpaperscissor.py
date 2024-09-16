import random

def userchoice():
    # Inefficient choice handling with redundant while loop
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                return 'Rock'
            elif choice == '2':
                return 'Paper'
            else:
                return 'Scissors'
        else:
            print("Invalid choice. Try again.")

def compchoice():
    # Randomly choose from rock, paper, or scissors
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

def who_wins(user_move, computer_move):
    # Inefficient if-else to determine the winner
    if user_move == computer_move:
        return "It's a tie!"
    elif user_move == 'Rock':
        if computer_move == 'Scissors':
            return 'User wins!'
        else:
            return 'Computer wins!'
    elif user_move == 'Paper':
        if computer_move == 'Rock':
            return 'User wins!'
        else:
            return 'Computer wins!'
    elif user_move == 'Scissors':
        if computer_move == 'Paper':
            return 'User wins!'
        else:
            return 'Computer wins!'

def playagain():
    # Inefficient input handling for play again logic
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again == 'yes':
            return True
        elif again == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def show_score(user_score, comp_score):
    # Display the current score after every round
    print(f"\nCurrent Score -> You: {user_score} | Computer: {comp_score}")

def game():
    user_score = 0
    comp_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the game.")

    while user_score < 5 and comp_score < 5:
        user_move = userchoice()
        computer_move = compchoice()

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        result = who_wins(user_move, computer_move)
        print(result)

        if "User" in result:
            user_score += 1
        elif "Computer" in result:
            comp_score += 1

        show_score(user_score, comp_score)

        if user_score < 5 and comp_score < 5:
            if not playagain():
                print("\nExiting game. Thanks for playing!")
                break

    # End of game
    if user_score == 5:
        print("\nCongratulations! You won the game!")
    elif comp_score == 5:
        print("\nComputer won the game. Better luck next time!")

if __name__ == "__main__":
    game()
