# Learn Python 3 the Hard Way

_Note: the contents of this repository were re-uploaded and originally completed on April of 2020 as part of another repository completely on my own._

The primary instruction resource is based on a PDF extraction of a book and online HTML webpage tutorial by the author __Zed Shaw__.
The questions are courtesy of [learnpythonthehardway.org](https://learnpythonthehardway.org/python3/), and one can obtain a copy of _Learn Python 3 the Hard Way_ there.


## Exercises
The following section will be concerned with the exercises of the tutorial: Learn Python 3 the Hard Way. It includes annotations of the self-explanatory tutorial rather than explanations.
Disclaimer: The set up process is very sophisticated, along with its Command Line Crash Course (in the appendix, page 288), could be put into a separate tutorial. Therefore, it will not be incorporated into this tutorial. Therefore, our first exercise will be on Page 34 of the PDF.
Here is a short Table of Contents.

Exercise No# | Exercise Name | Page Number
---:|---|:---:
1 | [A Good First Program][ex-1] | 34
2 | [Comments and Pound Characters][ex-2] | 40
3 | [Numbers and Math][ex-3] | 42
4 | [Variable and Names][ex-4] | 46
5 | [More Variables and Printing][ex-5] | 50
6 | [Strings and Text][ex-6] | 52
7 | [More Printing][ex-7] | 56
8 | [Printing, Printing][ex-8] | 60
9 | [Printing, Printing, Printing][ex-9] | 62
10 | [What Was That?][ex-10] | 64
11 | [Asking Questions][ex-11] | 68
12 | [Prompting People][ex-12] | 70
13 | [Parameters, Unpacking, Variables][ex-13] | 72
14 | [Prompting and Passing][ex-14] | 76
15 | [Reading Files][ex-15] | 80
16 | [Reading and Writing Files][ex-16] | 84
17 | [More Files][ex-17] | 88
18 | [Names, Variables, Code, Functions][ex-18] | 92
19 | [Functions and Variables][ex-19] | 96
20 | [Functions and Files][ex-20] | 100
21 | [Functions Can Return Something][ex-21] | 104
22 | [What Do You Know So Far?][ex-22] | 108
23 | [Strings, Bytes, and Character Encodings][ex-23] | 110
24 | [More Practice][ex-24] | 118
25 | [Even More Practice][ex-25] | 112
26 | [Congratulations, Take a Test!][ex-26] | 126
27 | [Memorizing Logic][ex-27] | 128
28 | [Boolean Practice][ex-28] | 132
29 | [What If][ex-29] | 136
30 | [Else and If][ex-30] | 138
31 | [Making Decisions][ex-31] | 142
32 | [Loops and Lists][ex-32] | 146
33 | [While Loops][ex-33] | 150
34 | [Accessing Elements of Lists][ex-34] | 154
35 | [Branches and Functions][ex-35] | 156
36 | [Designing and Debugging][ex-36] | 160
37 | [Symbol Review][ex-37] | 162
38 | [Doing Things to Lists][ex-38] | 168
39 | [Dictionaries, Oh Lovely Dictionaries][ex-39] | 174
40 | [Modules, Classes, and Objects][ex-40] | 180
41 | [Learning to Speak Object-Oriented][ex-41] | 186
42 | [Is-A, Has-A, Objects, and Classes][ex-42] | 192
43 | [Basic Object-Oriented Analysis and Design][ex-43] | 198
44 | [Inheritance Versus Composition][ex-44] | 214
45 | [You Make a Game][ex-45] | 224
46 | [A Project Skeleton][ex-46] | 228
47 | [Automated Testing][ex-47] | 236
48 | [Advanced User Input][ex-48] | 240
49 | [Making Sentences][ex-49] | 248
50 | [Your First Website][ex-51] | 256
51 | [Getting Input from a Browser][ex-52] | 264
52 | [The Start of Your Web Game][ex-53] | 274

_52/52 exercises uploaded_

Notes:
* ex37: Draw.io is used to create flowcharts. The file 'Python Default Flowchart Template.drawio' is a template for writing flowcharts for Python. When adding flowcharts, both the .drawio file and the exported file will be added to GitHub.

Todos:
- [x] Figure out Exercise 23 "Very Difficult" Challenge (still a no :confused:) <–– NVM I think I figured it out <–– Update! I did! :rofl:
- [ ] Change/Format all ex_information.txt files to .md files.
- [x] Finish Exercises 1-26 (Beginner)
- [x] Finish Exercises 27-44 (Intermediate)
- [ ] Finish Exercises 45-52 (Advanced)
- [ ] Add attributions to Zed Shaw in each exercise file.
- [x] More markdown integration! @stephi8013
  - [ ] Write an explanatory README.md File for each Exercise/Folder
  - [ ] Write a collective markdown file as a recap for everything (concise and helpful).

# Summary

Here is a Summary of each exercise, made as concise as possible while covering key points from the exercises.

### Exercise 1

Print text to the console using `print()`

A `str` or String is a sequence of characters placed within quotes (e.g. `"Hello, world"`).

- Inside apostrophes `' '` (single quotes), double quotes are ignored.
- Inside double quotes `" "`, apostrophes (single quotes) are ignored.

So this would be valid

```python
In[1]: print("I didn't")
In[2]: print('he said "go over there"')
```

```
Out[1]: I didn't
Out[2]: he said "go over there"
```

### Exercise 2

A # (called Octothrope, Pound, Hash, or Mesh.) is a comment

Code after a comment on the same line will not be executed by the compiler.

Comments could be put at the end of a line of code.

```python
print("Hello, world!")  # And here is a comment
```

### Exercise 3

Basic Arithmetic Operators

Operand Name | Operand | Purpose
:-|:-:|:-
Plus | `+` | Addition
Minus | `-` | Subtraction
Slash | `/` | Division
Double Slash | `//` | Floor Division – Quotient w/o Remainder
Asterisk | `*` | Multiplication
Double Asterisk | `**` | Exponentiation
Percent | `%` | Modulo (?)
Less-than | `<` | Comparison Smaller
Greater-than | `>` | Comparison Larger
Less-than-equal | `<=` | Comparison Smaller or Equivalent
Greater-than-equal | `>=` | Comparison Larger or Equivalent

Operands can be used inside functions, equivalence operators returns a Boolean (`True` or `False`) value.

Inside `print()`, a Plus `+` concatenates while a Comma `,` interpolates strings.

```python
In[1]: print("Is 3+2 greater than 6?", 3 + 2 > 6)
In[2]: print("What is 3+4?", 3 + 4)
```

```
Out[1]: Is 3+2 greater than 6? False
Out[2]: What is 3+4? 7
```

### Exercise 4

Variables could be assigned. Their definition syntax is `name = value` where name is the name of the variable and value is the data assigned to the value.

An `int` is an integer (e.g. `1`), while a `float` is a floating decimal number (e.g. `0.1`)

### Exercise 5

F-strings are one of the ways to fill in strings with other values. An F-string is just a string with the character `f` in front of the quotes. Inside an F-string, curly brackets `{}` store variables (or other values).

```python
In[1]: greeting = "Hello World"
In[2]: first_number = 4
In[3]: second_number = 5
In[4]: print(f"{greeting}! The sum of {first_number} and {second_number} is {first_number + second_number}.")
```

```
Out[1]: Hello World! The sum of 4 and 5 is 9.
```

### Exercise 6

The other way to format a string is by calling the `.format()` method on the string. This allows template strings to be stored inside variables, and formatted when called.

```python
In[1]: template = "There once was a {} who {}."
In[2]: print(template.format('boy', 'skates'))
In[3]: print("Hello there, {}!".format("David"))
```

```
Out[2]: There once was a boy who skates.
Out[3]: Hello there, David!
```

### Exercise 7

In python, a shorthand for concatenating a string upon itself any number of times can be achieved with the asterisk `*`.

To prevent the `print()` function from causing a new line (_by default_) at the end of the printed string, specify `end=''` or any other specification at the end of the print function.

```python
In[1]: print('-' * 10, end=', ')
In[2]: print(('<' + '>') * 10)
```

```
Out[1 and 2]: ----------, <><><><><><><><><><>
```

### Exercise 8

For template `.format()` strings, Refer to Exercise 6

### Exercise 9

Triple quotes can extend between lines. They have other uses as well (as comments and documentation for module functions). There are triple apostrophes `''' '''` and triple quotes `""" """`.

```python
In[1]: text = '''Hello,
>World
>!!!'''
In[2] print(text)
In[3] print("""Print
>Multiline
>Text.""")
```

```
Out[2]: Hello,
        World
        !!!
Out[3]: Print
        Multiline
        Text.
```

For escape sequences, Refer to Exercise 10.

### Exercise 10

In python, there are escape sequences for some special characters, including tabs and newlines.

```python
In[1]: tabbed = "\tTabbed Text."
In[2]: print(tabbed)
In[3]: print("Useful\nText\nWith\nNewlines.")
```

```
Out[2]:     Tabbed Text.
Out[3]: Useful
        Text
        With
        Newlines.
```

List of Escape Sequences

Sequence | Description
:-:|:-
`\\`|Returns \
`\'`|Returns '
`\"`|Returns "
`\a`|Returns ASCII bell (BEL)
`\b`|Returns ASCII backspace (BS)
`\f`|Returns ASCII formfeed (FF)
`\n`|Returns ASCII linefeed (LF)
`\N{name}`|Returns Character named name in the Unicode Database only
`\r`|Carriage Return (CR)
`\t`|Horizontal tab (TAB)
`\uxxxx`|Character with 16-bit hex value xxxx
`\Uxxxxxxxx`|Character with 32-bit hex value xxxxxxxx
`\v`|ASCII vertical tab (VT)
`\ooo`|Character with octal value ooo
`\xhh`|Character with hex value hh

### Exercise 11

The function `input()` prompts the console for input and returns it as a string. The input takes a string parameter to be the prompt.

```python
In[1]: input_text = input()
In[2]: name = input("What's Your Name?\n")
In[3]: print(f"Hi {name}, you said \"{input_text}\"")
```

_Note_: The input is typed in by the user.

```
Out[1]: Hello, world!
Out[2]: What's Your Name?
        Tom
Out[3]: Hi Tom, you said "Hello, world!"
```

### Exercise 12

For the function `input()`, Refer to Exercise 11.

For f-strings, Refer to Exercise 5.

### Exercise 13

`argv` is a `sys` System module that checks for input argument when executing the script, the parameters, unless enclosed as a string, are separated via spaces. `argv` is a list with the user inputs in order.

To use `argv`, it has to be imported first, as with all other packages. In this case, it is imported from the `sys` module.

```python
In[1]: from sys import argv
In[2]: script, first, second, third = argv
In[3]: print("The script is called: ", script)
In[4]: print("Your first variable is: ", first)
In[5]: print("Your second variable is: ", second)
In[6]: print("Your third variable is: ", third)
```

In line 2, we also see another way of unpacking lists: by assigning each index of a list a variable in order.

Programs like these cannot be run directly in the IDE, which cannot pass arguments when executing a file. They have to be run in a shell (denoted with a `$` sign)

```
$ python3 ex13.py Uno Zwei Trois
Out[3]: The script is called: ex13.py
Out[4]: Your first variable is: Uno
Out[5]: Your second variable is: Zwei
Out[6]: Your third variable is: Trois
```

### Exercise 14

For the function `input()`, Refer to Exercise 11.

For the module `argv`, Refer to Exercise 13.

### Exercise 15

To open a file, one has to call the `open()` function.

It is easiest to manipulate a file by assigning its open object to a variable. After it is assigned, the file can be read from the variable. When finished, make sure that the file is formally closed within the program.

When opening files, always specify permissions as a positional argument after the file path. 'r' is for read, 'a' is for append, and 'w' is for write (will truncate file), add a 'b' behind any of those three for reading and modifying binary files.

_Assuming there is a text file named "sample.txt" in the current working directory,_

```python
In[1]: filepath = "sample.txt"
In[2]: file = open(filepath, 'r')  # Could also do: file = open("sample.txt", 'r')
In[3]: print(file.read())
In[4]: file.close()
```

```
Out[3]: File Contents Listed Here
```

### Exercise 16

For file modes and permissions, Refer to Exercise 15 (and binary mode)

Mode | Permissions
:-:|:-
`'r'` | Read: can only read the file
`'a'` | Append: can only append to a file (writable seek always at EOF) *
`'w'` | Write: can write and truncate a file *
`'r+'` | Can read and write
`'a+'` | Can read, and write only at end of file *
`'w+'` | Can read and write *

_\*: Creates file if it doesn't exist_

File actions:

Method | Description
:-:|:-
`file.close()` | Saves and Closes file 'x'.
`file.read()` | Reads content of file/variable 'x' and returns result.
`file.readline()` | Reads and returns just one line of file (with defining parameter).
`file.truncate()` | Empties (and removes) contents of file 'x' (Beware!).
`file.write(content)` | Writes content to file.
`x.seek(0)` | Moves the read/write location to the beginning of file 'x'.
`x.seek(n)` | Moves the read/write location to the nth character of file 'x'.

### Exercise 17

For file actions/methods, Refer to Exercise 16.

Example: Make a copy of a file in one line given `from_file` and `to_file`

```python
out_file = open(to_file, 'w').write(open(from_file).read())
```

### Exercise 18

Functions are initiated with `def` and can perform actions and return values. Functions are mostly used to reduce repetitiveness in code. A function is "_called_" when it is used.

```python
In[1]: def print_two(arg1, arg2):
>          print(f"arg1: {arg1}, arg2: {arg2}")
In[2]: print_two("Apple", "Banana")
```

```
Out[2]: arg1: Apple, arg2: Banana
```

_Note_: Refer to Function Checklist for reminders when calling and defining functions.

### Exercise 19

For functions, Refer to Exercise 18

For number datatypes and arithmetic operators, Refer to Exercise 3

### Exercise 20

For functions, Refer to Exercise 18

For file actions/methods, refer to Exercise 16

### Exercise 21

Same as Exercise 19

### Exercise 22 (Review)

### Exercise 23

Concept: UTF-8 is an ASCII format that "_escapes_" to unicode (a larger, space consuming format with more symbols from other languages and emojis).

Mnemonic: "**DBES**" **Decode Bytes, Encode Strings**. **Decode** bytes in a alphanumerically (_ASCII_) represented binary format to get **Strings**, **Encode** strings to store them as **Bytes**.

In Python, the datatype _bytes_ are represented by an enclosing `b' '`. Type `byte` has the method `.decode(encoding=utf-8, errors=strict)` (where the arguments can be changed from the defaults by specifically referencing them) and type `str` has the method `.encode(encoding=utf-8, errors=strict)`

There are a few more self explanatory methods to data encoding that will be presented in the examples. Refer to the exercise for greater detail.

```python
# ASCII
In[1]: print(0b1011010)
Out[1]: 90

In[2]: print(format(90, 'b'))
Out[2]: 1011010

In[3]: print(int(1011010, 2))
Out[3]: 90

In[4]: ord('Z')
Out[4]: 90

In[5]: chr(90)
Out[5]: 'Z'

# UNICODE
In[6]: ord('')
Out[6]: 63743

In[7]: chr(63743)
Out[7]: ''

In[8]: to_encode = ''

In[9]: print(to_encode.encode(encoding=utf-8, errors=strict))
Out[9]: b'\xef\xa3\xbf'

In[10]: to_decode = b'\xef\xa3\xbf'

In[11]: print(to_decode.decode(encoding=utf-8, errors=strict))
Out[11]: ''

In[12]: print(type(to_decode))
Out[12]: <class 'bytes'>
```

### Exercise 24

Same as 19.

### Exercise 25

[List Operations](https://docs.python.org/3/tutorial/datastructures.html)

In Python, lists are defined using square brackets `[]`. They can comprise of any mix of data types, and they are _mutable_

Method | Description | Equivalent to
:-:|:-|:-:
`list.append(x)` | Add an item to the end of the list. | `a[len(a):] = [x]`
`list.extend(iterable)` | Extend the list by appending all the items from the iterable. | `a[len(a):] = iterable`
`list.insert(i, x)` | inserts item x to position/index i | E.g. `a.insert(len(a), x)` = `a.append(x)`
`list.remove(x)` | Remove the first item from the list whose value is equal to x, ValueError if not x in list. |
`list.pop([i])` | Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. | E.g. `list.pop(0)` = `list.popleft()`
`list.clear()` | Remove all items from the list. | `del a[:]`
`list.index(x[, start[, end]])` | Return zero-based index in the list of the first item whose value is equal to x. Raises ValueError if not x in list. |
`list.count(x)` | Return the number of times x appears in the list. |
`list.sort(key=None, reverse=False)` | Sort the items of the list in place (the arguments can be used for sort customization |
`list.reverse()` | Reverse the elements of the list in place.
`list.copy()` | Return a shallow copy of the list. | `a[:]`

_Notes:_
- `list.insert(0, x)` inserts x to the start of the list
- The square brackets around the i in the method signature of `list.pop()` denote that the parameter is optional, not that square brackets should be typed at that position. This notation will seen frequently in the Python Library Reference.
- See [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) for the explanation of the sorting arguments of method `list.sort()`

### Exercise 26 (Test)

### Exercise 27

This Exercise is about Logic and Truth Values (Conditionals)

Truth Terms:

<b>
* and
* or
* not
* != (not equal)
* == (equal)
* \>= (greater-than-equal)
* <= (less-than-equal)
* True
* False
</b>

Important Truth Tables to Remember:

<center>

**NOT** | **True?**
:---:|:---
_not_ False | True
_not_ True | False

**OR** | **True?**
:---:|:---
True _or_ True | True
True _or_ False | True
False _or_ True | True
False _or_ False | False

**AND** | **True?**
:---:|:---
True _and_ True | True
True _and_ False | False
False _and_ True | False
False _and_ False | False

_popularly referred to as **NOR**_

**NOT OR** | **True?**
:---:|:---
_not_ (True _or_ True) | False
_not_ (True _or_ False) | False
_not_ (False _or_ True) | False
_not_ (False _or_ False) | True

_popularly referred to as **NAND**_

**NOT AND** | **True?**
:---:|:---
_not_ (True _and_ True) | False
_not_ (True _and_ False) | True
_not_ (False _and_ True) | True
_not_ (False _and_ False) | True


And two more charts dealing with equality:

**!=** | **True?**
:---:|:---
1 != 1 | False
1 != 0 | True
0 != 1 | True
0 != 0 | False

**==** | **True?**
:---:|:---
1 == 1 | True
1 == 0 | False
0 == 1 | False
0 == 0 | True

</center>

### Exercise 28

Equality Operators:

Operator | Name | Description
:-:|:-|:-
`==` | equal | If the values of two operands are equal, then the condition becomes true.
`!=` | unequal | If values of two operands are not equal, then condition becomes true.
`>` | greater-than | If the value of left operand is greater than the value of right operand, then condition becomes true.
`<` | less-than | If the value of left operand is less than the value of right operand, then condition becomes true.
`>=` | greater-than-equal | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
`<=` | less-than-equal | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

Binary Operators:

Operator | Name | Description
:-:|:-|:-
`&` | Binary AND | Operator copies a bit to the result if it exists in both operands
`|` | Binary OR | It copies a bit if it exists in either operand.
`^` | Binary XOR | It copies the bit only if it is set in one operand and not both.
`~` | Binary Ones Complacent | It is unary and has the effect of 'flipping' bits.
`<<` | Binary Shift Left | The left operands value is moved left by the number of bits specified by the right operand. (This numerically multiplies by 2 per digit moved)
`>>` | Binary Shift Right | The left operands value is moved right by the number of bits specified by the right operand. (This numerically divides by 2 per digit moved)

### Exercise 29

If Statements Syntax should look something like this:

```python
if conditional:
    action
elif conditional:
    action
elif conditional:
    action
else:
    action
```

As many `elif` else if blocks can be nested as needed. `action`s are commands that are executed if their `conditional` is `True`. The if statements are executed **in order**, meaning that if more than one `conditional` is True, the first one in order will be executed.

### Exercise 30

For if-statements, Refer to Exercise 29.

### Exercise 31

Same as 30 and 19.

_Note_: `sys.exit()` is a System Module that quits a script. It takes an input (most commonly a number) as an exit code. `0` means no errors have occurred, that it is just a normal part of the script. While other cardinals refer to some sort of error.

### Exercise 32

For lists, Refer to Exercise 25.

**For Loops** are the most intuitive loops. They iterate something some number of times while executing the code block within itself each iteration. It is better to think of for loops as iterating lists, as the for loop can also iterate through values in a list. Their basic syntax is as follows.

```python
for range:
    actions

for value in list:
    actions(value)
```

The `range()` function takes two arguments, start and stop: `range(start, stop)`. It will describe the range [start, stop), more specifically for integers: [start, stop - 1]

In the second example, value is equivalent to the value of the list at the index that is currently being iterated.

List Unpacking Reminder: `*list` will unpack the contents of list one by one (as an _iterable_).

### Exercise 33

For for loops, Refer to Exercise 32.

### Exercise 34

For lists, Refer to Exercise 25.

For for loops, Refer to Exercise 32.

### Exercise 35

same as 34, 30, and 19.

### Exercise 36 (Writing Practice)

For flow charts, Ref#!

### Exercise 37 (Review)

Data Types:

Type | Description | Example
:-:|:-|:-
bytes | Stores bytes, maybe of text, PNG, file, etc. | `x = b"hello"`
dicts | Stores a key=value mapping of things. | `e = {'x': 1, 'y': 2}`
False | False boolean value. | `False and True == False`
floats | Stores decimals. | `i = 10.389`
lists | Stores a list of things. | `j = [1,2,3,4]`
None | Represents ”nothing” or ”no value”. | `x = None`
numbers | Stores integers. | `i = 100`
strings | Stores textual information. | `x = "hello"`
True | True boolean value. | `True or False == True`

Old (Python 2) String Formats (using %)

Escape | Description | Example
:-:|:-|:-
`%%` | A percent sign. | `"%g%%" % 10.34 == '10.34%'"`
`%c` | Character format. | `"%c" % 34 == '"'`
`%d` | Decimal integers (not floating point). | `"%d" % 45 == '45'`
`%e` | Exponential notation, lowercase ’e’. | `"%e" % 1000 == '1.000000e+03'`
`%E` | Exponential notation, uppercase ’E’. | `"%E" % 1000 == '1.000000E+03'`
`%f` | Floating point real number. | `"%f" % 10.34 == '10.340000'`
`%F` | Same as %f. | `"%F" % 10.34 == '10.340000'`
`%g` | "Either %f or %e, whichever is shorter. | `%g" % 10.34 == '10.34'`
`%G` | Same as %g but uppercase. | `"%G" % 10.34 == '10.34'`
`%i` | Same as %d. | `"%i" % 45 == '45'`
`%o` | Octal number. | `"%o" % 1000 == '1750'`
`%r` | Repr format (debugging format). | `"%r" % int == "<type 'int'>"`
`%s` | String format. | `"%s there" % 'hi' == 'hi there'"`
`%u` | Unsigned decimal. | `"%u" % -1000 == '-1000'"`
`%x` | Hexadecimal lowercase. | `"%x" % 1000 == '3e8'`
`%X` | Hexadecimal uppercase. | `"%X" % 1000 == '3E8'`


Special (somewhat uncommon) Operators:

Operator | Description | Example
:-:|:-|:-
`+=` | Add and assign | `x = 1; x += 2`
`@` | At (decorators) | `@classmethod`
`/=` | Divide and assign | `x = 10; x /= 2; x == 5`
`==` | Equal | `4 == 5 == False`
`//=` | Floor divide and assign | `x = 24; x //= 4; x == 1`
`//` | Floor division | `9 // 5 == 0`
`%=` | Modulus assign | `x = 99; x %= 20; x == 19`
`*=` | Multiply and assign | `x = 5; x *= 2; x == 10`
`!=` | Not equal | `4 != 5 == True`
`**=` | Power assign | `x = 5; x **= 3; x == 125`
`**` | Power of | `2 ** 4 == 16`
`%` | String interpolate or modulus | `2 % 4 == 2`
`-=` | Subtract and assign | `x = 1; x -= 2; x == -1`

Interesting Functions:
_The use of these functions were not explicitly referred to in the book. Reference links will be included for all of them_

Function | Short Description
:-:|:-
[`break`][pydoc_break_continue] | Breaks out of the innermost enclosing for or while loop. Will nullify the loops else statement, if any.
[`continue`][pydoc_break_continue] | Skip to the next iteration (if applicable) of a loop without processing more of the current iteration.
[`compile()`][pydoc_compile] | Compiles larger chunks of code for evaluation.
[`eval()`][pydoc_eval] | Evaluates a single expression.
[`exec()`][pydoc_exec] | Evaluates one "line"/block of code.
[`global`][pydoc_global] | Allows modification of a variable from a module-level scope. Avoids UnboundLocalError, placed inside local scopes.
[`lambda`][resource_lambda] | Creates an anonymous function, can only have one expression that is returned. Examples: `lambda arguments: expression`. Can be used as a function object by defining it equal to a variable or input when a function is required as an argument.
[`nonlocal`][pydoc_nonlocal] | Allows modification of a variable from a scope that is one higher its current.
[`pass`][pydoc_pass] | A placeholder for a function/class without actions/methods yet.
[`raise`][pydoc_raise] | Raises an exception (error) when things go wrong.
[`try: except: else: finally:`][pydoc_try] | Tries a block, Except handles errors in python from a Try block, Else is triggered when Try fails, and Finally is the cleanup block that gets executed regardless.
[`with-as:`][pydoc_with_as] | A convenient code block that makes cleanup easier with error/exception handling, and automatically closing opened files.
[`yield:`][pydoc_yield] | Returns a value to the caller. Good for iterating over large amounts of value one at a time without caching all the data in RAM. A function using yield within its definition is a **generator** function.


<!--References:-->
[pydoc_break_continue]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
[pydoc_compile]: https://docs.python.org/3/library/functions.html#compile
[pydoc_eval]: https://docs.python.org/3/library/functions.html#eval
[pydoc_exec]: https://docs.python.org/3/library/functions.html#exec
[pydoc_global]: https://docs.python.org/3/reference/simple_stmts.html#grammar-token-global-stmt
[resource_lambda]: https://www.programiz.com/python-programming/anonymous-function
[pydoc_nonlocal]: https://docs.python.org/3.2/reference/simple_stmts.html#grammar-token-nonlocal_stmt
[pydoc_pass]: https://docs.python.org/3.2/reference/simple_stmts.html#the-pass-statement
[pydoc_raise]: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
[pydoc_try]: https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
[pydoc_with_as]: https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
[pydoc_yield]: https://docs.python.org/3/reference/expressions.html#yield-expressions
<!--Scopes REF: https://www.programiz.com/python-programming/global-local-nonlocal-variables-->

_Notes_:
- Unlike an if-statement's `else` clause, which runs when none of the above conditions are met, a `try` statement's `else` clause runs when no exceptions are raised, a `for` loop's `else` clause runs when no breaks occur.

- In a function, if a `finally` clause specifies a return value, that will always be returned.

### Exercise 38

For lists, Refer to Exercise 25.

_Note_: Check here for [how bracket slices work](https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html).

Syntax: `sequence [start:stop[:step]]` Where start and stop are indices using 0-indexing (starting from 0) and step defaults to 1.

### Exercise 39

In Python, a dictionary is defined using the curly brackets `{}`

Dictionary Methods:

Method | Description
:-|:-
`dict.clear()` | Removes all the elements from the dictionary.
`dict.copy()` | Returns a copy of the dictionary.
`dict.fromkeys()` | Returns a dictionary with the specified keys and value.
`dict.get()` | Returns the value of the specified key.
`dict.items()` | Returns a list containing a tuple for each key value pair.
`dict.keys()` | Returns a list containing the dictionary's keys.
`dict.pop()` | Removes the element with the specified key.
`dict.popitem()` | Removes the last inserted key-value pair.
`dict.setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
`dict.update()` | Updates the dictionary with the specified key-value pairs.
`dict.values()` | Returns a list of all the values in the dictionary.

### Exercise 40

##### Modules are like Dictionaries

Custom modules can be imported in Python. Similar to a dictionary, a module is a python file that could be imported in another python script. The syntax of importing is as follows:

```python
import my_stuff

from my_stuff import *
```

Here's a hypothetical example of what `my_stuff` could contain.
```python
class Apples():

    def __init__(self):
        pass


def hello_world:
    print("Hello, world!")


bananas = "tasty!"
```

In the first import method, the contents could be accessed as such.

```python
In[1]: import mystuff

In[2]: x = my_stuff.Apples()

In[3]: my_stuff.hello_world()
Out[3]: Hello, world!

In[4]: print(mystuff.bananas)
Out[4]: tasty!
```

And in the second import method, the contents could be directly accessed using their name

```python
In[1]: bananas = "bland."

In[2]: from my_stuff import *

In[3]: x = Apples()

In[4]: hello_world()
Out[4]: Hello, world!

In[5]: print(bananas)
Out[5]: tasty!
```

As seen above, the second line caused `my_stuff.bananas` to be imported as `bananas`, overriding the original `bananas` which had a value of `"bland."`. This clashing is problematic, which is why the first method is preferred. However, if the file path or file name is very long, it could be imported under a shorter nickname for the module.

```python
In[1]: bananas = "bland."

In[2]: import my_stuff as m

In[3]: x = m.Apples()

In[4]: m.hello_world()
Out[4]: Hello, world!

In[5]: print(bananas)
Out[5]: bland.

In[6]: print(m.bananas)
Out[6]: tasty!
```

When importing from a directory other than the current working directory, include a file entitiled `__init__.py` in the same directory as the module and set Python's path to the current working directory. This could be achieved on Linux/Mac via `export PYTHON=$PYTHONPATH .`

##### Classes are like Modules

Classes in Python are an integral part of its Object Oriented Programming. To define a class, use the statement `class`. Inside the class, if variables have to be defined, a `__init__()` function needs to be called. The function takes arguments `self` and any other input variables the class wants at definition. Classes without inheritance are always defined as `object`s because:

> Explicit is better than implicit.

<div style="text-align: right">
- Line 2 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>

```python
class Person(object):
    def __init__(self, name, age, height_inches):
        self.name = name
        self.age = age
        self.height_cm = height_inches * 2.54
        self.weight = None
        self.job = None

    def print_resume():
        if self.job:
            print("{} currently work as a {}".format(self.name, self.job))
        else:
            print(f"{name} is currently unemployed")

    def grow_taller(height_in_cm):
        try:
            self.height_cm += height_in_cm
            print(f"you are now {self.height_cm} cm tall!")
        except ValueError
            print("Value Error: Are you sure you inputted a number?")
```

To initialize this example class, it needs to be called with three positional input parameters/arguments.

```python
In[1]: john = Person("John", 34, 72)

In[2]: print(john.height_cm)
Out[2]: 182.88

In[3]: john.job = "Technician"

In[4]: john.print_resume()
Out[4]: John currently work as a Technician

In[5]: john.grow_taller(10)  # Increase height by 10cm, yay!
Out[5]: you are now 192.88 cm tall!

In[6]: john.grow_taller('Technician')
Out[6]: Value Error: Are you sure you inputted a number?
```

When the Person john was defined, it is created as an object–an _instantiation_ of Person. In this case, john is-a Person. john has-a name, john has-a heigh (cm), john has-an age, and we defined john's job as a technician so john has-a job. This is the oversimplified version of `is-a` and `has-a` relationship between classes or classes and instances of such classes.

This is the basic demonstration of how Classes work in Python. They are fairly flexible and scalable as they are good for reducing redundant code.

### Exercise 41 (Review)

### Exercise 42 (Practice)

### Exercise 43 (A Game)

**Programming Processes:**

**The "Top-Down" Process:**

This process starts from the very abstract loose idea and then slowly refines it until the idea is solid and something that can be coded.

1. Write or draw about the problem.
2. Extract key concepts from 1 and research them.
3. Create a class hierarchy and object map for the concepts.
4. Code the classes and a test to run them.
5. Repeat and refine.

<br />

**The "Bottom-Up Process"**

This process is better once one is more solid at programming and are naturally thinking in code about problems.

1. Take a small piece of the problem; hack on some code and get it to run
barely.
2. Refine the code into something more formal with classes and automated tests.
3. Extract the key concepts being used and try to find research for them.
4. Write a description of what’s really going on.
5. Go back and refine the code, possibly throwing it out and starting over.
6. Repeat, moving on to some other piece of the problem.

### Exercise 44

There are two ways in which classes interact with one another: Inheritance and Composition.

##### Inheritance

Inheritance is when a class has an "is-a" relationship to another class. by defining `class Foo(Bar):` we are essentially saying `Foo` is-a `Bar`, and using a function called `super()` the _subclass/child class_ `Foo` will inherit all the attributes of _base class/parent class_ `Bar`.  (_Note: Terminology in Italics_)

There are three ways a base class and its subclass can interact via inheritance:

1. Implicit Inheritance

```python
class Parent(object):

    def implicit(self):
        print("PARENT implicit")


class Child(Parent):

    pass


dad = Parent()
son = Child()
```

```python
# This is a method of Parent and dad is-a Parent.
In[1]: dad.implicit()
Out[1]: PARENT implicit

# son inherited the trait implicitly from Parent because son is-a Child and class Child is-a Parent
In[2]: son.implicit()
Out[2] PARENT implicit
```

Remember:

> Explicit is better than implicit.

<div style="text-align: right">
- Line 2 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>

2. Override Explicitly

    An inherited trait can always be overridden by another definition.

```python
class Parent(object):

    def override(self):
        print("PARENT override")


class Child(Parent):

    def override(self):
        print("CHILD override")


dad = Parent()
son = Child()
```

```python
# This is a method of Parent and dad is-a Parent.
In[1]: dad.override()
Out[1]: PARENT override

# son overridden the inherited trait of 'override()' from class Parent.
In[2]: son.override()
Out[2] PARENT override
```

3. Alter Before and After
    Doing so essentially overrides the implicit trait by defining another trait with the same name. However, the parent trait is still in use because we referenced it with the `super()` function. `super(name, self)` where name is the name of the current class will return a parent class. Then, the `altered()` trait is called on that parent class. This method is better than implicit inheritance as it does not limit to the same name or exact traits. As many traits could be referenced as necessary, and any number of commands could be placed between theses references.

```python
class Parent(object):

    def altered(self):
        print("PARENT altered")


class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered")


dad = Parent()
son = Child()
```

```python
# This is a method of Parent and dad is-a Parent.
In[1]: dad.override()
Out[1]: PARENT altered

# son overridden the inherited trait of 'override()' from class Parent.
In[2]: son.override()
Out[2]: CHILD, BEFORE PARENT altered
        PARENT altered
        CHILD, AFTER PARENT altered
```

For more on the `super()` function, check this [brief explanation][super-1] or the [python documentations][pydoc_super].

<!--References-->
[super-1]: https://python-reference.readthedocs.io/en/latest/docs/functions/super.html
[pydoc_super]: https://docs.python.org/3.3/library/functions.html#super

##### Composition

Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance. Observing the three ways to exploit inheritance, two of the three
involve writing new code to replace or alter functionality. This can easily be replicated by just calling functions in a module.

```python
class Other(object):

    def override(self):
        print("OTHER override")

    def implicit(self):
        print("OTHER implicit")

    def altered(self):
        print("OTHER altered")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD, BEFORE OTHER altered")
        self.other.altered()
        print("CHILD, AFTER OTHER altered")

son = Child()
```

```python
In[1]: son.implicit()
Out[1]: OTHER implicit

In[2]: son.override()
Out[2]: CHILD override

In[3]: son.altered()
Out[3]: CHILD, BEFORE OTHER altered
        OTHER altered
        CHILD, AFTER OTHER altered
```

In this case, we defined the class `self.other()` as `Other()`; therefore, we can use `self.other()` to use and call any traits from class `Other`.

##### When it is appropriate to use each method.

1. Avoid multiple inheritance at all costs, as it is too complex to be reliable.
If there are no other options, then be prepared to know the class hierarchy and spend
time finding where everything is coming from.

2. Use composition to package code into modules that are used in many different
unrelated places and situations.

3. Use inheritance only when there are clearly related reusable pieces of code
that fit under a single common concept or if it is mandatory.

### Exercise 45 (Making a Game)

### Exercise 46

**_For exercises 46-51, refer to their exercises folder for an in-depth explanation._**

A virtual environment allows the testing and installation of packages with a _virtual_ installation of the native version of Python. In case anything goes wrong, no harm is done to the computer's main installation of python. Moreover, it is fairly easy and convenient to switch between multiple environments to test multiple packages and use different modules. To create a Virtual Environment, enter the following into a shell. _Note_: `venvs` is now a standard part of the Python 3 Installation.

```bash
mkdir ~/.venvs
python3 -m venvs ~/venvs/dir_name
```

Where `dir_name` is the name of the virtual environment.

To set up a skeleton for a python project, create the following file structure inside the project folder (usually `~/Projects`).

```
.
├── bin
├── doc
├── NAME
│   └── __init__.py
├── setup.py
└── tests
    ├── __init__.py
    └── NAME_tests.py
```

### Exercise 47

#### Follow this general loose set of guidelines when making tests:

Start the test file by importing nose tests and importing the project module/file to test.
```python
from nose.tools import *
from NAME.module import thing
```
Where `thing` is the specific class/part to be tested.

1. Test files go in tests/ (of the project's directory) and are named BLAH_tests.py, otherwise nose tests won’t run them, a safety measure to prevent nose tests from clashing with other program files.
2. Write one test file for each module.
3. Keep test cases (functions) short, and it is acceptable for test cases to be somewhat unorganized, as they usually tend to be.
4. Even though test cases are messy, try to keep them clean and remove any repetitive code possible. Create helper functions that get rid of duplicate code – that will be vital when the test script needs to be altered as duplicated code will make modifying tests more difficult.
5. Finally, do not get too attached to the tests. Sometimes, the best way to redesign something is to just delete it and start over.

The module `nosetests` will check whether two objects A and B are equal by calling `assert_equal(A, B)` in the test script during the testing.

If a module cannot be imported within the script, try `export PYTHONPATH=.` on Mac/Linux terminals.

### Exercise 48

A simplified version of the English language could include the following elements:
- Words separated by spaces.
- Sentences composed of the words.
- Grammar that structures the sentences into meaning.

In the game there needs to be a list of allowable words called a ”lexicon”:
- Direction words: north, south, east, west, down, up, left, right, back
- Verbs: go, stop, kill, eat
- Stop words: the, in, of, from, at, it
- Nouns: door, bear, princess, cabinet
- Numbers: any string of 0 through 9 characters

The words split-up from a sentence will be stored as tuples, an immutable file structure like an array. These are handy as they will display the words as a `(TYPE, WORD)` pair, facilitating the manipulation of the words.

_Note_: A **Tuple** is just a List that is immutable, a tuple cannot be modified. tuples are an essential part to Python's data processing/storing.

### Exercise 49

In this exercise, a parser is created that will break down a sentence (using the lexicon from last exercise) and attempts the understand the sentence using English's SVO – Subject Verb Object sentence structure and the manipulation of arrays made of `(TYPE, WORD)` tuples.

In this exercise, a special exception was defined for the parser. To define an exception, simply define it as a class that is-a Exception.

```python
class customError(Exception):

    def __init__(self, more_args):
        pass  # Define something
```

### Exercise 50

First, a web framework named `flask` has to be installed.

The term ”framework” generally means ”some package that makes it easier for one to do something.”

to install flask, make sure the Virtual Environment is activated. Execute the following command:

```bash
pip install flask
```

For some more information on flask, refer to the explanations within Exercises 50 and 51. This exercise only touched on the surface of flask, and not much information has been given. _A Django notes file may be coming soon_

### Exercise 51

The concept of "sessions" is used to store data from users and beautify URLs by removing the ugly specifications at the end of a link.

### Exercise 52 (gothonweb game Refactored)

<br />

<br />

# Coding Rules/Checklists:

### Functions Checklist:

1. Did you start your function with "def"?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you "end" your function by going back to writing with no indent ("dedenting", we call it)

When you run (”use” or ”call”) a function, check these things:

1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?

### Rules for If-Statements

1. Every if-statement must have an else.
2. If this else should never run because it doesn’t make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.
3. Never nest if-statements more than two deep and always try to do them one deep.
4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
5. Your Boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.

### Rules for Loops

1. Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over

### Tips for Debugging

1. Do not use a ”debugger.” A debugger is like doing a full-body scan on a sick person. You do not get any specific useful information, and you find a whole lot of information that doesn’t help and is just confusing.
2. The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.
3. Make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little.

The best way to work on a piece of software is in small chunks like this:
1. On a sheet of paper or an index card, write a list of tasks you need to complete to finish the software. This is your to do list.
2. Pick the easiest thing you can do from your list.
3. Write out English comments in your source file as a guide for how you would accomplish this task in your code.
4. Write some of the code under the English comments.
5. Quickly run your script so see if that code worked.
6. Keep working in a cycle of writing some code, running it to test it, and fixing it until it works.
7. Cross this task off your list, then pick your next easiest task and repeat.
This process will help you work on software in a methodical and consistent manner. As you work, update your list by removing tasks you don’t really need and adding ones you do.


# Code Style Guide for Independent Programming

### Function Style Guidelines:

* For various reasons, programmers call functions that are part of classes ”methods”. It’s mostly marketing, but just be warned that every time you say ”function” they’ll annoyingly correct you and say ”method.” If they get too annoying, just ask them to demonstrate the mathematical basis that determines how a ”method” is different from a ”function” and they’ll shut up.
* When you work with classes much of your time is spent talking about making the class ”do things.” Instead of naming your functions after what the function does, instead name it as if it’s a command you are giving to the class. Same as `pop` is saying ”Hey list, pop this off.” It isn’t called `remove_from_end_of_list` because even though that’s what it does, that’s not a command to a list.
* Keep your functions small and simple. For some reason when people start learning about classes they forget this.

### Class Style:

* Your class should use ”camel case” like `SuperGoldFactory` rather than `super_gold_factory`.
* Try not to do too much in your `__init__` functions. It makes them harder to use.
* Your other functions should use ”underscore format,” so write `my_awesome_hair` and `notmyawesomehair` or `MyAwesomeHair`.
* Be consistent in how you organize your function arguments. If your class has to deal with users, dogs, and cats, keep that order throughout unless it really doesn’t make sense. If you have one function that takes (`dog, cat, user`) and the other takes (`user, cat, dog`), it’ll be hard to use.
* Try not to use variables that come from the module or globals. They should be fairly self-contained.
* A foolish consistency is the hobgoblin of little minds. Consistency is good, but foolishly following some idiotic mantra because everyone else does is bad style. Think for yourself.
* Always ,_always_ have `class Name(object)` format or else you will be in big trouble.

### Code Style:

* Give your code vertical space so people can read it. You will find some very bad programmers who are able to write reasonable code but who do not add _any_ spaces. This is bad style in any language because the human eye and brain use space and vertical alignment to scan and separate visual elements. Not having space is the same as giving your code an awesome camouflage paint job.
* If you can’t read it out loud, it’s probably hard to read. If you are having a problem making something easy to use, try reading it out loud. Not only does this force you to slow down and really read it, but it also helps you find difficult passages and things to change for readability.
* Try to do what other people are doing in Python until you find your own style.
* Once you find your own style, do not be a jerk about it. Working with other people’s code is part of being a programmer, and other people have really bad taste. Trust me, you will probably have really bad taste too and not even realize it.
* If you find someone who writes code in a style you like, try writing something that mimics that style.

### Good Comments:

* Programmers will tell you that your code should be readable enough that you do not need comments. They’ll then tell you in their most official sounding voice, ”Ergo one should never write comments or documentation. QED.” Those programmers are either consultants who get paid more if other people can’t use their code, or incompetents who tend to never work with other people. Ignore them and write comments.
* When you write comments, describe _why_ you are doing what you are doing. The code already says how, but why you did things the way you did is more important.
* When you write doc comments for your functions, make the comments documentation for someone who will have to use your code. You do not have to go crazy, but a nice little sentence about what someone can do with that function helps a lot.
* While comments are good, too many are bad, and you have to maintain them. Keep your comments relatively short and to the point, and if you change a function, review the comment to make sure it’s still correct.


# Next Up

Things to learn beyond Basic Python:

- **Intermediate Python** (Zed Shaw LPTHW)

- **Flask** or **Django** (Flask is better and strongly recommended for beginners)

- **Scipy** (Anaconda/Jupyterlabs and Python's Math Syntax)

- **Pandas** (Data Manipulation, Replacement for Excel)

- **NLTK**(Natural Language Tool Kit) and **Tensorflow** (For Deep Learning/Neural Networks)

- **Pygame** (For creating graphical games using a sprite system)


<!--References-->

<!--Links-->
[ex-1]: Exercises/Exercise 01
[ex-2]: Exercises/Exercise 02
[ex-3]: Exercises/Exercise 03
[ex-4]: Exercises/Exercise 04
[ex-5]: Exercises/Exercise 05
[ex-6]: Exercises/Exercise 06
[ex-7]: Exercises/Exercise 07
[ex-8]: Exercises/Exercise 08
[ex-9]: Exercises/Exercise 09
[ex-10]:
[ex-11]:
[ex-12]:
[ex-13]:
[ex-14]:
[ex-15]:
[ex-16]:
[ex-17]:
[ex-18]:
[ex-19]:
[ex-20]:
[ex-21]:
[ex-22]:
[ex-23]:
[ex-24]:
[ex-25]:
[ex-26]:
[ex-27]:
[ex-28]:
[ex-29]:
[ex-30]:
[ex-31]:
[ex-32]:
[ex-33]:
[ex-34]:
[ex-35]:
[ex-36]:
[ex-37]:
[ex-38]:
[ex-39]:
[ex-40]:
[ex-41]:
[ex-42]:
[ex-43]:
[ex-44]:
[ex-45]:
[ex-46]:
[ex-47]:
[ex-48]:
[ex-49]:
[ex-50]:
[ex-51]:
[ex-52]:
