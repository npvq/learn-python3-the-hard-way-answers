from nose.tools import *
import ex48.lexicon as lexicon
from random import randint


def test_directions():
    for i in lexicon.directions:  # Tests for individual words
        assert_equal(lexicon.scan(i), [('direction', i)])

    result = lexicon.scan(str(' '.join(lexicon.directions).upper()))
    anticipated = []
    for i in lexicon.directions:  # Tests for string and case
        anticipated.append(('direction', i.upper()))

    assert_equal(result, anticipated)


def test_verbs():
    for i in lexicon.verbs:  # Tests for individual words
        assert_equal(lexicon.scan(i), [('verb', i)])

    result = lexicon.scan(str(' '.join(lexicon.verbs).upper()))
    anticipated = []
    for i in lexicon.verbs:  # Tests for string and case
        anticipated.append(('verb', i.upper()))

    assert_equal(result, anticipated)


def test_stops():
    for i in lexicon.stops:  # Tests for individual words
        assert_equal(lexicon.scan(i), [('stop', i)])

    result = lexicon.scan(str(' '.join(lexicon.stops).upper()))
    anticipated = []
    for i in lexicon.stops:  # Tests for string and case
        anticipated.append(('stop', i.upper()))

    assert_equal(result, anticipated)


def test_nouns():
    for i in lexicon.nouns:  # Tests for individual words
        assert_equal(lexicon.scan(i), [('noun', i)])

    result = lexicon.scan(str(' '.join(lexicon.nouns).upper()))
    anticipated = []
    for i in lexicon.nouns:  # Tests for string and case
        anticipated.append(('noun', i.upper()))

    assert_equal(result, anticipated)


def test_numbers():
    numberlist = []
    anticipated = []

    for i in range(10):
        number = randint(0, 99999)
        assert_equal(lexicon.scan(str(number)), [('number', number)])
        numberlist.append(str(number))
        anticipated.append(('number', number))

    numberstring = ' '.join(numberlist)
    result = lexicon.scan(numberstring)
    assert_equal(result, anticipated)


def test_errors():
    nonesense = ['D7sbdf', 'x897sDIods&', '()Cxhud', 'p@{10wfd8}', '8cx9jsf']
    index = randint(1, 5)
    assert_equal(lexicon.scan(nonesense[index]),
                 [('error', nonesense[index])])
    result = lexicon.scan(nonesense[0] + " bear " + nonesense[1] + " princess "
                          + nonesense[2])
    assert_equal(result, [('error', nonesense[0]),
                          ('noun', 'bear'),
                          ('error', nonesense[1]),
                          ('noun', 'princess'),
                          ('error', nonesense[2])])
