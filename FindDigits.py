#!/usr/bin/env python3
fobj = open("/tmp/String.txt")
digits = []
for word in fobj.read():
    if word.isdigit():
        digits.append(word)
print(''.join(digits))
fobj.close()
