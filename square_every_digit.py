def square_digits(num):
    arr = [digit for digit in str(num)]
    ret = ""
    for digit in arr:
        n = int(digit) ** 2
        ret += str(n)
    return int(ret)