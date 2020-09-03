from nose.tools import *
import ex49.lexicon as lexicon
import ex49.parser as parser


def sentence_equivalent(sentence1, sentence2):
    if sentence1.subject == sentence2.subject and sentence1.verb == sentence2.verb and sentence1.object == sentence2.object:
        return True

    return False


def test_game_sentences():
    sentences = []
    sentences.append((parser.parse_sentence(lexicon.scan("The bear eat the princess")),
                      parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess'))))
    sentences.append((parser.parse_sentence(lexicon.scan("Kill the bear")),
                      parser.Sentence(('noun', 'player'), ('verb', 'Kill'), ('noun', 'bear'))))
    sentences.append((parser.parse_sentence(lexicon.scan("The bear go to 1234")),
                      parser.Sentence(('noun', 'bear'), ('verb', 'go'), ('number', 1234))))
    sentences.append((parser.parse_sentence(lexicon.scan("The bear stop a door from opening")),
                      parser.Sentence(('noun', 'bear'), ('verb', 'stop'), ('noun', 'door'))))
    for i in sentences:
        assert_equal(sentence_equivalent(i[0], i[1]), True)


def test_calling_exceptions():
    raw = lexicon.scan("The donkey would like to eat")
    assert_raises(parser.ParserError, parser.parse_subject, raw)
