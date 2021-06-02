from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['pile', 'patent', 'combination', 'illustrate', 'forestry', 'old', 'midnight', 'explode', 'divorce', 'gift', 'calm', 'cherry', 'apology', 'meadow',
                 'extract', 'gallery', 'preparation', 'root', 'hospitality', 'party', 'code', 'smooth', 'cellar', 'art', 'broadcast', 'reason', 'die', 'document', 'sniff', 'table']


def _get_random_word(list_of_words):
    return random.choice(list_of_words)


def _mask_word(word):
    if word:
        return ''.join(['*' for letter in range(len(word))])
    else:
        raise InvalidWordException('Invalid Word')


def _uncover_word(answer_word, masked_word, character):
    if not answer_word and not masked_word:
        raise InvalidWordException('Words shouldn\'t be empty')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Words should be the same length')
    if len(character) != 1:
        raise InvalidGuessedLetterException('Invalid guess')
    
    if character.lower() in answer_word.lower() and character.lower() not in masked_word.lower():
        
        masked_list = list(masked_word)

        for i, c in enumerate(answer_word):
            if c.lower() == character.lower():
                masked_list[i] = c.lower()
        return ''.join(masked_list)

    return masked_word

    


def guess_letter(game, letter):
    # game was already over
    if game['remaining_misses'] <= 0:
        raise GameFinishedException('Game is already over')
    
    # save previous masked word to compare to _uncover_word result
    previous_masked = game['masked_word']

    # check if guess was correct and store guess
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    game['previous_guesses'].append(letter.lower())

    #check if incorrect guess
    if previous_masked == game['masked_word']:
        game['remaining_misses'] -= 1

        # game is lost if no more guesses
        if game['remaining_misses'] <= 0:
            raise GameLostException()

    # game is won if masked word == answer word
    if game['masked_word'] == game['answer_word']:
        raise GameWonException()



def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
