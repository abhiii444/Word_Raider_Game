"""
Word Raider - A Word Guessing Game
Similar to Wordle: Guess a 5-letter word in 6 attempts
"""

# Import required modules
import random  # For selecting random words
import os      # For clearing the screen

# ANSI color codes for terminal output
# These make the game visually appealing with colored feedback
GREEN = '\033[92m'   # Correct letter in correct position
YELLOW = '\033[93m'  # Correct letter in wrong position
GRAY = '\033[90m'    # Letter not in word
RESET = '\033[0m'    # Reset color to default
BOLD = '\033[1m'     # Bold text

# List of 5-letter words for the game
# In a real game, you'd have a much larger word list
WORD_LIST = [
    'apple', 'brain', 'charm', 'dance', 'earth',
    'flame', 'grace', 'heart', 'image', 'jolly',
    'knife', 'light', 'magic', 'night', 'ocean',
    'piano', 'queen', 'river', 'storm', 'tiger',
    'unity', 'voice', 'water', 'youth', 'zebra',
    'beach', 'cloud', 'dream', 'eagle', 'frost',
    'ghost', 'honey', 'index', 'jewel', 'karma',
    'lemon', 'maple', 'north', 'olive', 'peace',
    'quilt', 'robot', 'snake', 'table', 'uncle',
    'valor', 'whale', 'xerox', 'yacht', 'zonal'
]


def clear_screen():
    """
    Clears the terminal screen for better game display
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def select_random_word():
    """
    Selects a random word from the word list
    Returns: A random 5-letter word in lowercase
    """
    return random.choice(WORD_LIST).lower()


def get_user_guess():
    """
    Gets a valid 5-letter guess from the user
    Keeps asking until a valid input is provided
    Returns: A valid 5-letter word in lowercase
    """
    while True:
        # Prompt user for input
        guess = input("\nEnter your 5-letter guess: ").strip().lower()
        
        # Validate the guess
        if len(guess) != 5:
            print(" Please enter exactly 5 letters!")
            continue
        
        if not guess.isalpha():
            print(" Please use only letters (no numbers or symbols)!")
            continue
        
        # Valid guess - return it
        return guess


def check_guess(guess, target_word):
    """
    Compares the guess with the target word and returns feedback
    
    Args:
        guess: The user's guessed word
        target_word: The correct word to guess
    
    Returns:
        A list of tuples: [(letter, status), ...]
        where status is 'correct', 'present', or 'absent'
    """
    result = []  # Will store feedback for each letter
    target_letters = list(target_word)  # Convert to list for manipulation
    
    # First pass: Mark all correct positions (green)
    for i in range(5):
        if guess[i] == target_word[i]:
            result.append((guess[i], 'correct'))
            target_letters[i] = None  # Mark as used
        else:
            result.append((guess[i], None))  # Placeholder
    
    # Second pass: Check for letters in wrong positions (yellow)
    for i in range(5):
        if result[i][1] is None:  # Not already marked as correct
            if guess[i] in target_letters:
                result[i] = (guess[i], 'present')
                # Remove first occurrence to handle duplicate letters correctly
                target_letters[target_letters.index(guess[i])] = None
            else:
                result[i] = (guess[i], 'absent')
    
    return result


def display_guess_with_colors(feedback):
    """
    Displays a guess with colored feedback
    Green = correct position
    Yellow = wrong position
    Gray = not in word
    
    Args:
        feedback: List of (letter, status) tuples from check_guess()
    """
    display = ""
    
    for letter, status in feedback:
        if status == 'correct':
            # Green background for correct position
            display += f"{GREEN}{BOLD} {letter.upper()} {RESET}"
        elif status == 'present':
            # Yellow background for wrong position
            display += f"{YELLOW}{BOLD} {letter.upper()} {RESET}"
        else:
            # Gray background for absent letter
            display += f"{GRAY}{BOLD} {letter.upper()} {RESET}"
    
    print(display)


def display_game_state(guesses, max_attempts):
    """
    Displays the current game state with all previous guesses
    
    Args:
        guesses: List of all guess feedbacks
        max_attempts: Maximum number of attempts allowed
    """
    print("\n" + "="*40)
    print(f"{'WORD RAIDER':^40}")
    print("="*40)
    print(f"\nAttempt {len(guesses)}/{max_attempts}\n")
    
    # Display all previous guesses
    for feedback in guesses:
        display_guess_with_colors(feedback)
    
    # Display remaining empty slots
    remaining = max_attempts - len(guesses)
    for _ in range(remaining):
        print(f"{GRAY} _ _ _ _ _ {RESET}")


def display_instructions():
    """
    Displays game instructions to the player
    """
    print("\n" + "="*50)
    print(f"{'WELCOME TO WORD RAIDER!':^50}")
    print("="*50)
    print("\n RULES:")
    print("  • Guess the 5-letter word in 6 attempts")
    print("  • After each guess, colors show how close you are:")
    print(f"    {GREEN}■{RESET} GREEN  = Correct letter in correct position")
    print(f"    {YELLOW}■{RESET} YELLOW = Correct letter in wrong position")
    print(f"    {GRAY}■{RESET} GRAY   = Letter not in the word")
    print("\n Let's play!\n")


def play_game():
    """
    Main game loop - runs one complete game
    Returns: True if player wins, False if player loses
    """
    # Game configuration
    MAX_ATTEMPTS = 6
    target_word = select_random_word()  # Select the word to guess
    guesses = []  # Store all guess feedbacks
    attempts = 0  # Current attempt number
    
    # Display instructions
    clear_screen()
    display_instructions()
    input("Press Enter to start...")
    
    # Main game loop
    while attempts < MAX_ATTEMPTS:
        clear_screen()
        display_game_state(guesses, MAX_ATTEMPTS)
        
        # Get user's guess
        guess = get_user_guess()
        attempts += 1
        
        # Check the guess
        feedback = check_guess(guess, target_word)
        guesses.append(feedback)
        
        # Check if player won
        if guess == target_word:
            clear_screen()
            display_game_state(guesses, MAX_ATTEMPTS)
            print(f"\n {GREEN}CONGRATULATIONS!{RESET} ")
            print(f"You guessed the word '{target_word.upper()}' in {attempts} attempts!")
            return True
    
    # Player lost - reveal the word
    clear_screen()
    display_game_state(guesses, MAX_ATTEMPTS)
    print(f"\n {GRAY}Game Over!{RESET}")
    print(f"The word was: {BOLD}{target_word.upper()}{RESET}")
    return False


def main():
    """
    Main function - handles game loop and replay logic
    """
    print("\n" + "="*50)
    print(f"{' WORD RAIDER ':^50}")
    print("="*50)
    
    # Game statistics
    games_played = 0
    games_won = 0
    
    # Play until user wants to quit
    while True:
        won = play_game()
        games_played += 1
        
        if won:
            games_won += 1
        
        # Display statistics
        print(f"\n Statistics:")
        print(f"   Games Played: {games_played}")
        print(f"   Games Won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"   Win Rate: {win_rate:.1f}%")
        
        # Ask if player wants to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print(f"\n Thanks for playing Word Raider!")
            print(f"Final Stats - Won {games_won}/{games_played} games")
            break


# Entry point of the program
if __name__ == "__main__":
    """
    This block runs only when the script is executed directly
    (not when imported as a module)
    """
    try:
        main()  # Start the game
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n Game interrupted. Thanks for playing!")
    except Exception as e:
        # Handle any unexpected errors
        print(f"\n An error occurred: {e}")
        print("Please report this bug!")