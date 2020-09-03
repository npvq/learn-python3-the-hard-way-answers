# Defining exception using class.
class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, object):
        # Remember, we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


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


def parse_verb(word_list):  # skips stop words, checks if next word is a verb.
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    elif next_word == 'number':
        return match(word_list, 'number')  # Added number integration
    else:
        raise ParserError("Expected a noun, direction, or number next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a noun or verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
