#Exercise 27: Logic
In this lesson we will be learning the basics of python programming logic and committing them to memory.

##The Truth Terms
In Python, there are a few terms to determine whether something is "True" or "False." Logic on a computer is all about seeing if some combination of these characters and some variables are true at a certain point in the program/execution. A few of those terms will be listed below.
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

##The Truth Tables
Here are a few applications of the truth terms, these are important to commit to memory.

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
