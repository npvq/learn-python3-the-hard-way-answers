# 1:
True and True  # True
# 2:
False and True  # False
# 3:
1 == 1 and 2 == 1  # False
# 4:
"test" == "test"  # True
# 5:
1 == 1 or 2 != 1  # True
# 6:
True and 1 == 1  # True
# 7:
False and 0 != 0  # False
# 8:
True or 1 == 1  # True
# 9:
"test" == "testing"  # False
# 10:
1 != 0 and 2 == 1  # False
# 11:
"test" != "testing"  # True
# 12:
"test" == 1  # False
# 13:
not (True and False)  # True
# 14:
not (1 == 1 and 0 != 1)  # False
# 15:
not (10 == 1 or 1000 == 1000)  # False
# 16:
not (1 != 10 or 3 == 4)  # False
# 17:
not ("testing" == "testing" and "Zed" == "Cool Guy")  # True
# 18:
1 == 1 and (not ("testing" == 1 or 1 == 0))  # True
# 19:
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))  # False
# 20:
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))  # False

# Evaluations are commented to the right of the expressions.

# Approach to evaluating Boolean Statements
#   1. Find an equality test (== or !=) and replace it with its truth.
#   2. Find each and/or inside parentheses and solve those first.
#   3. Find each not and invert it.
#   4. Find any remaining and/or and solve it.
#   5. When you are done you should have True or False.

# Shortcuts (stop there = go no further)
# Any AND expression that has a False is immediately False, stop there.
# Any or expression that has a True is immediately True, stop there.
