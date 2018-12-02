def repeat_frequency(changes):
    s = 0
    seen_vals = set([0])
    while True:
        for n in changes:
            s += n
            if s in seen_vals:
                return s
            seen_vals.add(s)

repeat_frequency([int(i) for i in open('input1.txt', 'r')])
