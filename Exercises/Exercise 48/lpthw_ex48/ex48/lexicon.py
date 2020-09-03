from string import punctuation

filter_table = str.maketrans('', '', punctuation)

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
              'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
# Heiarchy: Numbers, Stops, Directions, Verbs, Nouns, Errs
# Didn't have to use try, except because used .isdigit() method of str.


def split_sentence(sentence):
    return sentence.split(' ')


def type(word):  # finds type of word, returns type/token (string)
    if word.isdigit():
        return 'number'
    elif word in stops:
        return 'stop'
    elif word in directions:
        return 'direction'
    elif word in verbs:
        return 'verb'
    elif word in nouns:
        return 'noun'
    else:
        return 'error'


def scan(input):
    words = split_sentence(input)
    output = []
    for word in words:
        # This is casefolded for evaluation purposes
        word_eval = word.casefold().translate(filter_table)
        if type(word) == 'number':
            word = int(word)
            # Another method would be to do int(float(word)) which is redundant.

        output.append((type(word_eval), word.translate(filter_table)))

    return output
