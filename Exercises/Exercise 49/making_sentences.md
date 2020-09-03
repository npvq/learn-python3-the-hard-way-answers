# Making Sentences

Structure of the English Language:
> Subject, Verb, Object


Obviously it gets more complex than that. What we want is to turn the preceding lists of tuples into a nice Sentence object that has subject, verb, and object.

## Match and Peek

To do this we need five tools:

1. A way to loop through the list of scanned words. That’s easy.
2. A way to ”match” different types of tuples that we expect in our Subject Verb Object setup.
3. A way to ”peek” at a potential tuple so we can make some decisions.
4. A way to ”skip” things we do not care about, like stop words.
5. A Sentence object to put the results in.

## Sentence Grammar

`Sentence.subject` This is the subject of any sentence but could default to ”player” most of the time since a sentence of ”run north” is implying ”player run north”. This will be a noun.

`Sentence.verb` This is the action of the sentence. In ”run north” it would be ”run”. This will be a verb.

`Sentence.object` This is another noun that refers to what the verb is done on. In our game we separate out directions which would also be objects. In ”run north” the word ”north” would be the object. In ”hit bear” the word ”bear” would be the object.

Our parser then has to use the functions we described and, given a scanned sentence, convert it into an **List** of Sentence objects to match the input.

## Exceptions

This code demonstrates how to do that with the ParserError at the top. Notice that it uses classes to give it the type of Exception. Also notice the use of the raise keyword to raise the exception.

## Contents

The contents of this exercise are stored in a project directory titled `lpthy_ex49`. The test script is written for the original parser `ex49/parser.py` (*from the book*) as the improved version `ex49/parser_improved.py` patched many bugs from its predecessor.
