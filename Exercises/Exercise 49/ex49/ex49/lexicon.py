# Improved for ex49.
from string import punctuation

filter_table = str.maketrans('', '', punctuation)

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
              'back']
verbs = ['go', 'stop', 'kill', 'eat']
# Added more stop words
stops = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
         'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they',
         'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
         'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who',
         'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below',
         'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
         'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our',
         'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she',
         'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
         'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then',
         'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not',
         'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too',
         'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
         'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it',
         'how', 'further', 'was', 'here', 'than']
nouns = ['door', 'bear', 'princess', 'cabinet']
# Heiarchy: Numbers, Stops, Directions, Verbs, Nouns, Errs
# Didn't have to use try, except because used .isdigit() method of str.


def split_sentence(sentence):
    return sentence.split(' ')


def token(word):  # finds type of word, returns type/token (string)
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
        word_eval = None
        # Int could not be "translated", so they are separated in conditional.
        if token(word) == 'number':  # <–– Changed logic structure
            word = int(word)
            output.append(('number', word))
        else:
            word_eval = word.casefold().translate(filter_table)
            output.append((token(word_eval), word.translate(filter_table)))
            # Another method would be to do int(float(word)) which is redundant.

    return output
