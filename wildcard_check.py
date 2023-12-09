import ps3

word_list = ps3.load_words()

def wildcard_check(word, word_list):
    match = False
    for list_word in word_list:
        if len(list_word) is not len(word):
            continue
        
        for n in range(len(list_word)):
            
            if list_word[n] is word[n]:
                match = True
            elif list_word[n] in ps3.VOWELS and word[n] is '*':
                match = True
            else:
                match = False
                break
           
        if match is True:
            print(list_word)
            return match
    return match

word = 's*andard'
print(wildcard_check(word, word_list))