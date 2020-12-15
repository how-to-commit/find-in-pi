def piGenerator():
    """Generator function outputs digits of pi"""
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1:
            yield int(d)
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


def cleanListToStr(lst):
    """Convert list to str and cleans output"""
    return str(lst).strip("[]").replace(", ", '')


def match(pattern, text):
    """Checks whether pattern is in text as a substring or a sublist
    pattern and text are both allowed to be either string or list."""
    cleanListToStr(pattern)
    cleanListToStr(text)
    return pattern in text


def verifyInput(number):
    """Checks whether input is a integer provided as str or list"""
    try:
        int(number)
        return True
    except ValueError:
        return False


def search(number, depth=-1):
    """Searches for passed in number in Pi."""
    counter = 0
    d_buffer = []

    while not (depth = 0):
        depth -= 1
        counter += 1

        for digit in piGenerator():
            d_buffer.append(digit)
            if match(d_find, d_buffer):
                position = counter - len(number)
                return (True, position)

            # purge useless digit from buffer to prevent slowdown at larger numbers
            if len(d_buffer) > len(d_find):
                d_buffer.pop(0)

    # Exit, could not find number within search depth
    return False