# English Language Module – Advanced User Input

It should be alright for a user to write something a lot like English for your game and have your game figure out what it means. To do this, we’re going to write a module that does just that. This module will have a few classes that work together to handle user input and convert it into something your game can work with reliably.

<br />

A simplified version of the English language could include the following elements:
- Words separated by spaces.
- Sentences composed of the words.
- Grammar that structures the sentences into meaning.

## Our Game Lexicon

In our game we have to create a list of allowable words called a ”lexicon”:
- Direction words: north, south, east, west, down, up, left, right, back
- Verbs: go, stop, kill, eat
- Stop words: the, in, of, from, at, it
- Nouns: door, bear, princess, cabinet
- Numbers: any string of 0 through 9 characters

## 1: Breaking up a Sentences

```python
stuff = input(’> ’)
words = stuff.split ()
```
This should do it for now, it mostly works well.

## 2: Lexicon Tuples

```python
first_word = (’verb’, ’go’)
second_word = ( ’ direction ’ , ’ north ’ )
third_word = (’direction’, ’west’)
sentence = [ first_word , second_word , third_word ]
```

We will be storing the words from a split-up sentence as tuples, an immutable file structure like an array. These are handy as they will help us view the words as a `(TYPE, WORD)` pair, facilitating our manipulation of the words.

## 3: Scanning Input

This scanner will take a string of raw input from a user and return a sentence that’s composed of a list of tuples with the (TOKEN, WORD) pairings. If a word isn’t part of the lexicon, then it should still return the WORD but set the TOKEN to an error token. These error tokens will tell users they messed up.

This is left as a challenge for the student to write.

## 4: Exceptions

```python
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
```

The the above scenario, if s is not an integer, it will return `None` to prevent the system from raising an error.

You put the code you want to ”try” inside the try block, and then you put the code to run for the error inside the except. In this case, we want to ”try” to call int() on something that might be a number. If that has an error, then we ”catch” it and return `None`.

## Contents

The contents of this exercise will be stored in a project directory entitled `lpthw_ex48`.

The original unit test file is renamed `tests/lexicon_test.old.py` and the improved unit test is named `tests/lexicon_test.py`. To run the old one, delete all the `x`s in front of the `test_` functions.
