def DNA_strand(dna):
    str = ""
    for char in dna:
        match char:
            case 'A':
                str += 'T'
            case 'T':
                str += 'A'
            case 'C':
                str += 'G'
            case 'G':
                str += 'C'
            case _:
                print("Wrong input")
    return (str)