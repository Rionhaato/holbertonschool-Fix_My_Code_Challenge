#!/usr/bin/python3
"""
FizzBuzz - Print the numbers from 1 to n separated by a space.

For multiples of three print "Fizz" instead of the number and for
multiples of five print "Buzz". For numbers which are multiples of both
three and five print "FizzBuzz".
"""


def fizzbuzz(n):
    """Return the FizzBuzz sequence from 1 to n."""
    tmp_result = []

    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))

    return tmp_result


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)

    print(" ".join(fizzbuzz(number)))
