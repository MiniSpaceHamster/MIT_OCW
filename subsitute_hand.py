import ps3

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
    alphabet = ps3.CONSONANTS + ps3.VOWELS
    sub_hand = hand.copy()
    if letter in hand:
        new_letter = ps3.random.choice(alphabet)
        print(new_letter)
        while new_letter in hand:
            new_letter = ps3.random.choice(alphabet)
            print(new_letter)
        sub_hand[new_letter] = hand[letter]
        del sub_hand[letter]
    return sub_hand

hand = {'h':1, 'e':1, 'l':2, 'o':1}
letter = 'l'
print(hand)
print(substitute_hand(hand, letter))