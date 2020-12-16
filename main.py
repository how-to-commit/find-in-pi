import logic


while True:
    d_find = input("Enter a string of numbers you want to find in Pi: ")
    while not (logic.verifyInput(d_find) and int(d_find) > 0):
        d_find = input("WARN: Enter positive numbers only.\nEnter a string of numbers you want to find in Pi: ")

    depth = input("Enter desired search depth (leave blank for default value or -1 to disable): ")
    while not logic.verifyInput(depth):
        depth = input("WARN: Enter numbers only.\nEnter desired search depth (leave blank for default value or -1 to disable): ")

    result = logic.search(d_find, depth)
    if not result:
        print("Could not find your digit in current search depth of {} digits.".format(depth))
    else:
        print("Your number has been found at position {}.".format(result[1]))
