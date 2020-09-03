# Defining exception using class.
class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, object):
        # Remember, we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


# word[0] specifies 'TYPE' in tuple '(TYPE, WORD)'
def peek(word_list):  # Takes the first word from list (sentence)
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return none


def match(word_list, expecting):  # Checks if matches expecting and returns word
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return none
    else:
        return None


def skip(word_list, word_type):  # skips stop words until finds next word/type.
    while peek(word_list) == word_type:
        match(word_list, word_type)


# Skips Type = Error and Stop
def skip_multi(word_list, word_types):
    while peek(word_list) in word_types:
        match(word_list, word_type)


class Parse():

    def __init__(self):
        pass

    # skips stop words, checks if next word is a verb.
    def verb(self, word_list):
        skip_multi(word_list, ['stop', 'error]')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParseError("Expected a verb next.")

    def object(self, word_list):
        skip_multi(word_list, ['stop', 'error]')
        next_word = peek(word_list)
        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParseError("Expected a noun or direction next.")

    def subject(self, word_list):
        skip_multi(word_list, ['stop', 'error]')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

    def sentence(self, word_list):
        subj = parse_subject(word_list)
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        return Sentence(subj, verb, obj)

# I like the methods method better than the class method because it is
# simpler and there is no need for an unused class template in a program
# comprising of multiple files.
