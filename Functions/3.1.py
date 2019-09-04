def right_justify(s):
    length_of_s = len(s)
    leading_space = " " * (70 - length_of_s)
    result = leading_space + s
    print(result)
right_justify('love')