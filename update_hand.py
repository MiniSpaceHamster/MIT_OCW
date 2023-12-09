import ps3

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
    # 1) Define new_hand as an empty dictionary.
    new_hand = {}
    
    # 2) Convert word to a dictionary where letters are keys and the freq is the value.
    word = ps3.get_frequency_dict(word)
    
    # 3) Iterate through keys in hand. For each letter, subtract word_freq value from hand value,
    # if the remaining_value is greater than zero(0), add the key and 
    # remaining_val to new_hand.
    remaining_val = 0
    for key in hand:
        print(key, ":", end=" ")
        print(hand.get(key, 0),"-", end=" ")
        print(word.get(key, 0), end=" ")
        remaining_val = hand.get(key, 0) - word.get(key, 0)
        print("=", remaining_val)
        if remaining_val > 0:
            new_hand[key] = remaining_val 
    return new_hand

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = "quail"
new_hand = update_hand(hand, word)
ps3.display_hand(new_hand)