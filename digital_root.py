def digital_root(n):
    while n > 9:
        arr = [digit for digit in str(n)]
        n = 0
        for digit in arr:
            n += int(digit)
    return n
        
# 				 538283895717559872
n = digital_root(5382838957175598633);
print(n)