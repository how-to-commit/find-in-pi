
def pi_gen():
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1:
            yield int(d)
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

def match(pattern, text):
    pattern = str(pattern).strip("[]")
    text = str(text).strip("[]").replace(", ", '')
    return pattern in text

while True:
    d_find = input("Enter a string of numbers you want to find in Pi: ")
    while not d_find.isnumeric():
        d_find = input("WARN: Enter numbers only.\nEnter a string of numbers you want to find in Pi: ")

    d_buf = []
    for digit in pi_gen():
        d_buf.append(digit)
        if match(d_find, d_buf):
            print("String {} is present from position {} to {} in Pi!".format(d_find, len(d_buf)-len(d_find), len(d_buf)-1))
            break