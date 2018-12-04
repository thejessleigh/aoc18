import re


def claims(input):
    side = 1000
    matrix = [["O" for x in range(side)] for y in range(side)]

    pattern = re.compile(r'#(?P<claim_id>\d*)\s@\s(?P<x>\d*),(?P<y>\d*):\s(?P<w>\d*)x(?P<h>\d*)')
    for claim in input.read().splitlines():
        claim_details = dict((k, int(v)) for k, v in pattern.search(claim).groupdict().items())
        y = claim_details['y']
        for _ in range(claim_details['h']):
            x = claim_details['x']
            for _ in range(claim_details['w']):
                if matrix[y][x] == "O":
                    matrix[y][x] = claim_details['claim_id']
                else:
                    matrix[y][x] = "X"
                x += 1
            y += 1
    return sum(x.count("X") for x in matrix)

claims(open('input.txt', 'r'))