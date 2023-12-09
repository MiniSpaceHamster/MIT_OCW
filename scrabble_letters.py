import math
import random
import string

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word, n, letter_values):
    
    # Convert word into lowercase.
    word = word.lower()

    # Iterate through the word as dictionary keys and store the sum value as component 1.
    comp1 = 0
    for letter in word:
        comp1 = comp1 + letter_values[letter]

    # Calculate component 2, compare to a value of 1, keep the higher value.
    comp2 = (7*len(word)) - (3*(n - len(word)))
    if comp2 < 1:
        comp2 = 1

    # Calculate and return the product of components 1 & 2.
    score = comp1*comp2
    return score

word = 'testing'
n = 10

print(get_word_score(word, n, SCRABBLE_LETTER_VALUES))