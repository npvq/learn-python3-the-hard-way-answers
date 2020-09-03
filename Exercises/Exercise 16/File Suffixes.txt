List of File Suffixes for Python 3
x.close()       Saves and Closes file 'x'
x.read()        Reads content of file/variable 'x' and returns result
x.readline()    Reads and returns just one line of file (with defining parameter)
x.truncate()    Empties (and removes) contents of file 'x' (Beware!)
x.write(y)      Writes y to file 'x'
x.seek(0)       Moves the read/write location to the beginning of file 'x'
x.seek(n)       (?) Moves the read/write location to the nth character of file 'x'

Opening files:
open(x, m)      Opens file 'x' in mode 'm'
                Default mode is 'r' for read
                There are also 'w' for write and 'a' for append
                The '+' modifier combines the modes: e.g. 'r+' 'w+' and 'a+'
