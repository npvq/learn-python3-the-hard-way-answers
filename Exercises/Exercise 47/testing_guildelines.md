# Testing Guidelines
#### From LPTHW Exercise 47

<br />

#### Follow this general loose set of guidelines when making your tests:

1. Test files go in tests/ and are named BLAH_tests.py, otherwise nose tests won’t run them. This also keeps your tests from clashing with your other code.
2. Write one test file for each module you make.
3. Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of messy.
4. Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper functions that get rid of duplicate code. You will thank me later when you make a change and then have to change your tests. Duplicated code will make changing your tests more difficult.
5. Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it and start over.

The module `nosetests` will check whether two objects A and B are equal when you call `assert_equal(A, B)` in the test script during the testing.

If you cannot import a module within your script, try `export PYTHONPATH=.` on Mac/Linux terminals.

The files used in this exercise is stored in `Exercise 47/` as `lpthw_ex47/`. Note that the `bin` and `doc` folders are not added because they are empty, and empty folders are ignored by GitHub.
