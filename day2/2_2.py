def mismatch(ids):
    lines = ids.read().splitlines()
    for line in lines:
        for other in lines:
            differing_chars = 0
            for index, value in enumerate(line):
                if value != other[index]:
                    differing_chars += 1
            if differing_chars == 1:
                return ''.join([value for index, value in enumerate(line) if value == other[index]])



print(mismatch(open('input.txt', 'r')))
