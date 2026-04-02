def kprimes_step(k, step, start, nd):
    stop = round(nd ** 0.5)
    primes = set()
    for number in range(start, nd + 1, 1):
        n = 2
        i = 0
        number_copy = number
        while number > 1 and n <= stop and i < k:
            if number % n == 0:
                number /= n
                i += 1
            else:
                n += 1
        if (i == k - 1 and number >= n) or (number == 1 and i == k):
            primes.add(number_copy)
    ret = []
    for number in sorted(primes):
        if number + step in primes:
            ret.append([number, number + step])
    return ret