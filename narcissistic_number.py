def narcissistic( value ):
    string = str(value)
    lenght = len(string)
    sum = 0
    
    for digit in string:
        sum += int(digit) ** lenght
        
    if sum == value:
        return True
    return False # Code away