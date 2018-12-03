import re

def claims(input):
    c = input.read().splitlines()
    side = 1000
    matrix = [["O" for x in range(side)] for y in range (side)]
    idx = r'\d*(,)\d*'
    dim = r'\d*(x)\d*'
    cl = r'(#)\d*'
    overlap = 0
    for claim in c:
        claimant = int(re.search(cl, claim).group(0)[1:])
        print(claimant)
        inidicies = [int(i) for i in re.search(idx, claim).group(0).split(',')]
        print(inidicies)
        dimensions = [int(i) for i in re.search(dim, claim).group(0).split('x')]
        print(dimensions)
        x = inidicies[0]
        y = inidicies[1]
        width = dimensions[0]
        height = dimensions[1]
        for _ in range(height):
            for _ in range(width):
                space = matrix[y][x]
                if space == "O":
                    matrix[y][x] = claimant
                else:
                    matrix[y][x] = "X"
                x += 1
            x = inidicies[0]
            y += 1
        check_overlap = 0
    for x in matrix:
        check_overlap += x.count("X")
    print(check_overlap)

    return overlap

print(claims(open('input.txt', 'r')))