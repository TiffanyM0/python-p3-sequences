#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    first = 0
    second = 1
    if length == 0 :
        print ([ ])
    elif length == 1 :
        print ([first])
    elif length == 2:
        print([first, second])      
    else:
        sequence = [0, 1]
        while len(sequence) < length:
            current_length = len(sequence)
            c = sequence[current_length - 1] + sequence[current_length - 2]
            sequence.append(c)
        # Return the list of Fibonacci numbers.
        print(sequence)

