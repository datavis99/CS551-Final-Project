import heapq
from collections import Counter

# Step 1: Load Words from words.txt
def load_words(word_list_file):
    with open(word_list_file, 'r') as f:
        words = [word.strip().lower() for word in f if word.strip()]
    return words

word_list = load_words('words.txt')

# Step 2: Define the Heuristic Function
def heuristic(candidate_words):
    """
    Heuristic function that scores words based on letter frequency.
    """
    letter_counts = Counter(''.join(candidate_words))
    def score(word):
        return -sum(letter_counts[c] for c in set(word))
    return score

# Step 3: Feedback Processing Functions
def get_feedback(guess, target):
    """
    Simulate Wordle feedback.
    Returns a string with 'G' for green, 'Y' for yellow, and 'B' for black.
    """
    feedback = ['B'] * 5
    target_letters = list(target)
    # First pass for correct positions (greens)
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = 'G'
            target_letters[i] = None
    # Second pass for present but misplaced letters (yellows)
    for i in range(5):
        if feedback[i] == 'B' and guess[i] in target_letters:
            feedback[i] = 'Y'
            target_letters[target_letters.index(guess[i])] = None
    return ''.join(feedback)

def update_possible_words(possible_words, guess, feedback):
    """
    Update the list of possible words based on the feedback from a guess.
    """
    new_possible_words = []
    for word in possible_words:
        match = True
        used_letters = [False]*5  # Track letters used for 'Y' feedback
        for i in range(5):
            if feedback[i] == 'G':
                if word[i] != guess[i]:
                    match = False
                    break
            elif feedback[i] == 'Y':
                if guess[i] == word[i] or guess[i] not in word:
                    match = False
                    break
                else:
                    idx = word.find(guess[i])
                    while idx != -1:
                        if guess[idx] != word[idx] and not used_letters[idx]:
                            used_letters[idx] = True
                            break
                        idx = word.find(guess[i], idx + 1)
                    else:
                        match = False
                        break
            elif feedback[i] == 'B':
                if guess[i] in word:
                    match = False
                    break
        if match:
            new_possible_words.append(word)
    return new_possible_words

# Step 4: Implement the A* Search Algorithm
def a_star_wordle_solver(target_word, valid_words):
    possible_words = valid_words.copy()
    guess_history = []
    heap = []
    heapq.heappush(heap, (0, [], possible_words))

    print('\n' + 'Selected Word: ' + target_word + '\n')
    
    while heap:
        cost, path, possible_words = heapq.heappop(heap)
        if path:
            last_guess = path[-1]
            feedback = get_feedback(last_guess, target_word)
            print(feedback)
            possible_words = update_possible_words(possible_words, last_guess, feedback)
        if not possible_words:
            continue
        if len(path) >= 6:
            break  # Exceeded maximum allowed guesses
        # Goal check
        if path and path[-1] == target_word:
            return path
        # Generate next guesses
        h_func = heuristic(possible_words)
        for word in possible_words:
            if word in path:
                continue
            heapq.heappush(heap, (cost + 1 + h_func(word), path + [word], possible_words))
    return None  # No solution found within 6 guesses

# Step 5: Get Target Word from User Input
user_input = input(f"\nEnter an index between 0 and {len(word_list) - 1}: ")

try:
    index = int(user_input)
    if 0 <= index < len(word_list):
        target_word = word_list[index]
    else:
        print("Index out of range.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Step 6: Allow User to Play Wordle if Desired
play_input = input("\nWould you like to play Wordle (Y/N)? ")

if play_input == 'Y':

    guess1 = None
    guess2 = None
    guess3 = None
    guess4 = None
    guess5 = None
    guess6 = None
    solved = False

    while guess1 == None:
        guess1 = input("\nEnter Guess #1: ")
        if guess1 not in word_list:
            print("Invalid guess. Not in word list!")
            guess1 = None
        if guess1 == target_word:
            solved = True
            print("You Win! Word:",target_word,"Guesses: 1")
        else:
            if guess1 != None:
                print(guess1,':',get_feedback(guess1,target_word))

    if solved != True:
        while guess2 == None:
            guess2 = input("\nEnter Guess #2: ")
            if guess2 not in word_list:
                print("Invalid guess. Not in word list!")
                guess2 = None
            if guess2 == target_word:
                solved = True
                print("You Win! Word:",target_word,"Guesses: 2")
            else:
                if guess2 != None:
                    print(guess2,':',get_feedback(guess2,target_word))

    if solved != True:
        while guess3 == None:
            guess3 = input("\nEnter Guess #3: ")
            if guess3 not in word_list:
                print("Invalid guess. Not in word list!")
                guess3 = None
            if guess3 == target_word:
                solved = True
                print("You Win! Word:",target_word,"Guesses: 3")
            else:
                if guess3 != None:
                    print(guess3,':',get_feedback(guess3,target_word))

    if solved != True:
        while guess4 == None:
            guess4 = input("\nEnter Guess #4: ")
            if guess4 not in word_list:
                print("Invalid guess. Not in word list!")
                guess4 = None
            if guess4 == target_word:
                solved = True
                print("You Win! Word:",target_word,"Guesses: 4")
            else:
                if guess4 != None:
                    print(guess4,':',get_feedback(guess4,target_word))

    if solved != True:
        while guess5 == None:
            guess5 = input("\nEnter Guess #5: ")
            if guess5 not in word_list:
                print("Invalid guess. Not in word list!")
                guess5 = None
            if guess5 == target_word:
                solved = True
                print("You Win! Word:",target_word,"Guesses: 5")
            else:
                if guess5 != None:
                    print(guess5,':',get_feedback(guess5,target_word))

    if solved != True:
        while guess6 == None:
            guess6 = input("\nEnter Guess #6: ")
            if guess6 not in word_list:
                print("Invalid guess. Not in word list!")
                guess6 = None
            if guess6 == target_word:
                solved = True
                print("You Win! Word:",target_word,"Guesses: 6")
            else:
                if guess6 != None:
                    print(guess6,':',get_feedback(guess6,target_word))
                    print("\nOut of Moves! Better Luck Next Time! Word:",target_word)
            
elif play_input == 'N':
    pass
else:
    print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
    exit()

# Step 7: Run the Wordle Solver
solution_path = a_star_wordle_solver(target_word, word_list)

# Step 8: Print the Result
if solution_path:
    print('\n' + f"Solved in {len(solution_path)} guesses: {solution_path}")
else:
    print("Failed to solve the Wordle puzzle within 6 guesses.")