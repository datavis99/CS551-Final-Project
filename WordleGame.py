import heapq
from collections import defaultdict, Counter

# Step 1: Load the Word List
def load_words(word_list_file):
    with open(word_list_file, 'r') as f:
        words = [word.strip().lower() for word in f if len(word.strip()) == 5 and word.isalpha()]
    return words

# For demonstration, let's assume 'words.txt' contains your word list
word_list = load_words(r"C:\Users\igene\CS551-Final-Project\words.txt")
valid_words = set(word_list)

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
        for i in range(5):
            if feedback[i] == 'G' and word[i] != guess[i]:
                match = False
                break
            elif feedback[i] == 'Y':
                if guess[i] == word[i] or guess[i] not in word:
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
    h_func = heuristic(possible_words)
    
    while heap:
        cost, path, possible_words = heapq.heappop(heap)
        if path:
            last_guess = path[-1]
            feedback = get_feedback(last_guess, target_word)
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

# Example Usage
target_word = 'crane'  # The word to guess
solution_path = a_star_wordle_solver(target_word, word_list)

if solution_path:
    print(f"Solved in {len(solution_path)} guesses: {solution_path}")
else:
    print("Failed to solve the Wordle puzzle within 6 guesses.")
