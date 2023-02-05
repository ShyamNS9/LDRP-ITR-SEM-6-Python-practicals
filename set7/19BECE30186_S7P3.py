# Set-7 Practical-3 : A text file contains a header line, few comments lines followed by actual lines of data. Write
# a python program to create a function skip_header() that skips the header and all the comment lines and prints only
# actual lines of data.

def skip_header():
    if line.startswith('#'):
        pass
    else:
        print(line)


with open('try.txt') as f:
    while line := f.readline():
        skip_header()