#Hangman Game Project
#Collaborator
#Sebastian Melendez Sifuentes

#Import the main libraries
import random
#Create Global variables
word_list = ["Apple", "Banana", "Pineapple", "Durian", "Watermelon", "Kiwi", "Strawberry"]
word_list2 = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
    'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
    'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule']
word_list3 = ['newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino',
    'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger',
    'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']
def main(): #Main structure of the Game
    print("The Hangman Game")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    #Set the game specifications for each level
    difficulty = {"1": (10, word_list), "2": (8, word_list2), "3": (6, word_list3)}
    #Loop for the user level selection and validation of input
    while True:
        level = input("Choose the game difficulty: ").strip()
        if level in difficulty:
            count, word = difficulty[level]
            word_r = random.choice(word).lower()#chose a random item from the list
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    current = ["_"]* len(word_r)
    g_l = []
    while count >0:

        if current.count("_")>0: #Check if the word is complete
            #Display the interface of the game
            print(f"Current word: {' '.join(current)}")
            print(f"Guessed letters: {", ".join(g_l)}")
            print(f"Incorrect guesses remaining: {count}")
            #Get the user input and validate it
            guess_w = input("Guess a letter: ").strip().lower()
            if len(guess_w) != 1:#Check if the input is more than 1 letter
                print("Invalid input. Please enter a single alphabet letter.")
                continue
            elif not guess_w.isalpha():#Check if the input is not in the alphabet
                print("Invalid input. Please enter a single alphabet letter.")
                continue
            elif guess_w in g_l:#Check if the input is already guessed
                print(f"You already guessed '{guess_w}'. Try a different letter.")
                continue
            #Save the input
            g_l.append(guess_w,)
            #Test if the letter is in the current word.
            if guess_w in word_r:
                for n,l in enumerate(word_r):
                    if l == guess_w:
                        current[n]= guess_w
                print(f"Good Work [{guess_w}] is in the word")
            else:
                count -= 1
                print(f"Sorry, [{guess_w}] is not in the word.")
        else:#When the player won
           print(f"Congratulations! You guessed the word: {word_r}")
           break
    else:#When the player fail
        print(f"Game over! The word was: {word_r}")


main()