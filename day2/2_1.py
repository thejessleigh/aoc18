def checksum(inputs):
    ids = inputs.read().splitlines()
    twos = 0
    threes = 0
    for row in ids:
        seen = {}
        for letter in row:
            seen[letter] = seen.get(letter, 0) + 1
        if 2 in seen.values():
            twos += 1
        if 3 in seen.values():
            threes += 1

    return twos * threes


print(checksum(open('input.txt', 'r')))
