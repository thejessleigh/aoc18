def resulting_frequency(changes):
    return sum([int(n) for n in changes])

resulting_frequency(open('input1.txt', 'r'))
