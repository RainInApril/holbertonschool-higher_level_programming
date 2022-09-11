#!/usr/bin/python3


for character in range(ord('z'), ord('a') - 1, - 1):
    if character % 2:
        print("{:c}".format(character - 32), end='')
    else:
        print("{:c}".format(character), end='')
