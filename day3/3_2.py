import re

def claims(input):
    c = input.read().splitlines()
    side = 1000
    matrix = [["O" for x in range(side)] for y in range (side)]
    idx = r'\d*(,)\d*'
    dim = r'\d*(x)\d*'
    cl = r'(#)\d*'
    all_ids = set()
    overlap_ids = set()
    for claim in c:
        claimant = int(re.search(cl, claim).group(0)[1:])
        all_ids.add(claimant)
        inidicies = [int(i) for i in re.search(idx, claim).group(0).split(',')]
        dimensions = [int(i) for i in re.search(dim, claim).group(0).split('x')]
        x = inidicies[0]
        y = inidicies[1]
        width = dimensions[0]
        height = dimensions[1]
        for _ in range(height):
            for _ in range(width):
                space = matrix[y][x]
                if space == "O":
                    # first claim to this space
                    matrix[y][x] = claimant
                elif space == 'X':
                    # claim overlaps with existing overlapped claim
                    overlap_ids.add(claimant)
                else:
                    # claim overlaps with exactly one preexisting claim
                    overlap_ids.add(claimant)
                    overlap_ids.add(space)
                    matrix[y][x] = "X"
                x += 1
            x = inidicies[0]
            y += 1
    return all_ids.difference(overlap_ids)

print(claims(open('input.txt', 'r')))