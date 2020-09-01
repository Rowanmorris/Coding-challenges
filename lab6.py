print('Welcome to the Pig Latin Translator!')
original_word = input('Enter a word to be translated: \n')


def koa(original_word):
    # if no text entered
    if original_word == "":
        print('there is nothing there')
        return

    pyg_latin = 'ay'
    # splits line into lowercase list
    word_list = original_word.lower().split()
    # will treat 'y' as vowel for now
    vowels = "aeiouy"

    # empty list to hold translated line
    result = []

    # loop over each word in word list
    for word in word_list:
        first = word[0]

        if first in vowels:
            word += 'w'
        # example word strong: word = ongstr
        elif word[1] not in vowels and word[2] not in vowels:
            word = word[3:] + word[0:3]
        # example word chase: word = asech
        elif word[1] not in vowels:
            word = word[2:] + word[0:2]
        else:
            word = word[1:] + word[0]

    
        new_word = word + pyg_latin
    
        result.append(new_word)

   
    translation = " ".join(result)
    print(translation[0].upper() + translation[1:] + ".")

    run_again = input('Translate another line? (yes or no): ')

    if run_again == 'yes':
        original_word = input('Enter a word:')
        koa(original_word)
    elif run_again == 'no':
        print('k')

koa(original_word)
