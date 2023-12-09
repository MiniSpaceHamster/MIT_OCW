# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : MiniSpaceHamster
# Collaborators : 
# Time spent    : 

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

#WORDLIST_FILENAME = "words.txt"
GOOGLE_FILENAME = 'G:\My Drive\Python\Python\MIT OCW\MIT OCW 6.0001\PS_3\words.txt'
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    #inFile = open(WORDLIST_FILENAME, 'r')
    inFile = open(GOOGLE_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

"""
def get_word_score(word, n, letter_values):
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
"""
def get_word_score(word, n, letter_value):
    
    # Convert word into lowercase.
    word = word.lower()

    # Iterate through the word as dictionary keys and store the sum value as component 1.
    comp1 = 0
    for letter in word:
        print('{} = {}'.format(letter, letter_value[letter]))
        comp1 = comp1 + letter_value[letter]
    print('Word score: {}'.format(comp1))
    # Calculate component 2, compare to a value of 1, keep the higher value.
    comp2 = (7*len(word)) - (3*(n - len(word)))
    if comp2 < 1:
        comp2 = 1
    print('7*{} letters - 3*({} hand - {} letters) = {}'.format(len(word), n, len(word), comp2))
    # Calculate and return the product of components 1 & 2.
    score = comp1*comp2
    print('{} x {} =  {}'.format(comp1, comp2, score))
    return score
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print('Your hand is: ', end='')
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3) - 1) # Subtract one vowel and insert an '*' into the hand.
    hand['*'] = 1
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Itterate through word as keys to hand and create new hand without word.
    new_hand = hand.copy()
    for letter in word:
        try: 
            new_hand[letter] = new_hand[letter] - 1
        except:
            continue   
        if new_hand[letter] < 1:
            del new_hand[letter]  
    return new_hand

#
# Problem #3: Test word validity
#   

def wildcard_check(word, word_list):
    match = False
    for list_word in word_list:
        # Check if the length of the words are the same.
        if len(list_word) is not len(word):
            continue
        # Itterate through the letters and confirm if they match.
        for n in range(len(list_word)):
            if list_word[n] is word[n]:
                match = True
            # Matching vowels and * count as a match in the word.
            elif list_word[n] in VOWELS and word[n] is '*':
                match = True
            else:
                match = False
                break
        if match is True:
            return match
    return match

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # Compare word to word list to confirm valid entry
    if '*' in word:
        if wildcard_check(word, word_list) is False:
            return False
    elif word not in word_list:
        return False
    
    # Convert word into a list and index against the hand.
    word_keys = get_frequency_dict(word)
    for key in word_keys:
        if hand.get(key, 0) < word_keys[key]:  
            return False
    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for key in hand:
        handlen += hand[key]
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    total_score = 0
    word = ''
    hand = hand
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list) is True:
                # Tell the user how many points the word earned,
                # and the updated total score
                n = calculate_handlen(hand)
                score = get_word_score(word, n, SCRABBLE_LETTER_VALUES)
                total_score += score
                print('word earned {} points. Total: {} points'.format(score, total_score))
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if word == '!!':
        print('You ended the hand. Total score: {}'.format(total_score))
    else:
        print('You ran out of letters. Total score: {}'.format(total_score))
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    alphabet = CONSONANTS + VOWELS + '*' # Adds all letters and wildcard to the letter pool.
    sub_hand = hand.copy()
    if letter in hand:
        new_letter = random.choice(alphabet)
        while new_letter in hand: # Confirms the new letter is not already in the hand.
            if new_letter is '*':
                break # Allows for multiple wildcards in the hand.
            new_letter = random.choice(alphabet)        
        sub_hand[new_letter] = hand[letter]
        del sub_hand[letter]
    return sub_hand 
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # Keep track of the total score for all hands played.
    # Set the total number of subsitutions allowed.
    # Set the number of hand replays allowed.
    total_score = 0
    subs = 1
    replays = 1
    # Ask user how many hands are to be played.
    total_hands = 0
    while total_hands < 1:
        try:
            total_hands = int(input('How many hands would you like to play? '))
        except:
            print('Please enter an integer greater than zero.')
    
    # While there are still hands to be played.
    while total_hands > 0:
        # Track the score for the current hand being played.
        hand_score = 0
        # Deal the hand.
        hand = deal_hand(10)
        # If there are still subsitutions left, display hand,
        # and ask the user if they would like to subsitute.
        if subs > 0:
            display_hand(hand)
            sub = input('Would you like to subsitute a letter (you may only do this {} per game)? '.format(subs))
            sub = sub.lower()
            if sub == 'yes' or sub == 'y':
                letter = input('Which letter would you like to replace? ')
                hand = substitute_hand(hand, letter)
                subs -= 1        
        # Play the hand.
        score = play_hand(hand, word_list)
        # If these are replays left ask the user if they would like to reply.
        if replays > 0:
            replay = input('Would you like to try for a better score this hand (you may only do this {} times per game)? '.format(replays))
            replay = replay.lower()
            if replay == 'yes' or replay == 'y':
                # Record previous score.
                previous_score = score
                # Replay hand.
                score = play_hand(hand, word_list)
                # Compare the new score with the previous score, keep the highest.
                if previous_score < score:
                    print('You scored higher than your previous score of {} points!'.format(previous_score))
                else:
                    # Display the highest score to the user.
                    print('Your previous score of {} points is higher.'.format(previous_score))
                    score = previous_score
        # Add score to the total score of all hands played.
        # Subtract this hand from the total number of hands played.
        total_score += score
        total_hands -= 1
    # Game is over, display the total score. Ridicule player no matter how high the score.
    print('Game over. Your total score is: {}'.format(total_score))
    print('You suck!')

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
