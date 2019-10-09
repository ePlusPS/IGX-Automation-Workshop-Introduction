#!/usr/bin/env python

# this imports the time module
import time
print('hello')
age = input('how old are you?: ')
time.sleep(5)
if int(age) > 21:
    print('Yoda says, much experience, you must have!')
else:
    print('Yoda says, young apprentice you are!')

