import ps3

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
    # 
    if word not in word_list:
        return False
    
    word = ps3.get_frequency_dict(word)
    for key in word:
        print(key, ': ')
        print(word[key])
        print(hand.get(key, 0))
        
        if hand.get(key, 0) < word[key]:
            return False
    return True
    
word_list = ps3.load_words()
hand = {'c':1, 'a': 2, 't': 1}
word = 'cowts'
print(is_valid_word(word, hand, word_list))