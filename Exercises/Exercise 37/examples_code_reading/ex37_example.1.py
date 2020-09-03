# This code 'Remove Duplicates' comes courtesy of Python Fiddle:
# http://pythonfiddle.com/remove-duplicates-function/
# It has been converted to Python 3 by hand, refer to documentation below:
# https://docs.python.org/2/library/2to3.html
# And edited to follow the style guidelines of 'pycodestyle'


def remove_duplicates(lista):
    lista2 = []
    if lista:
        for item in lista:  # iterates list a
            if item not in lista2:  # is item in lista2 already?
                lista2.append(item)
                # Only appends item to list a2 if it isn't already there.
    else:
        return lista
    return lista2


print(remove_duplicates([1, 2, 3, 3]))

# You can use a list as a conditonal statement
# "In Python, empty lists evaluate to 'False' and none-empty lists evaluate
#  to 'True' in Boolean contexts. Therefore, we can simply treat the list as a
#  predicate returning a Boolean value. This solution is highly pythonic and
#  reccommended by PEP8 Style Guide"
# Source: https://www.techiedelight.com/check-list-empty-python/
# PEP8 Style Guide: https://www.python.org/dev/peps/pep-0008/
