def patternToNumber(pattern):
    # A = 0
    # C = 1
    # G = 2
    # T = 3

    sum = 0

    pattern = pattern[::-1]

    i=0
    for base in pattern:
        if base is 'A':
            sum += 0 * 4**i
        else:
            if base is 'C':
                sum += 1 * 4 ** i
            else:
                if base is 'G':
                    sum += 2 * 4 ** i
                else:
                    sum += 3 * 4 ** i

        i = i+1

    return sum

print(patternToNumber('CCATAGATCAACAGAGGTTCTTCAGACGT'))


####################################################################


def patternToNumber(pattern):
    # A = 0
    # C = 1
    # G = 2
    # T = 3

    sum = 0

    pattern = pattern[::-1]

    i=0
    for base in pattern:
        if base is 'A':
            sum += 0 * 4**i
        else:
            if base is 'C':
                sum += 1 * 4 ** i
            else:
                if base is 'G':
                    sum += 2 * 4 ** i
                else:
                    sum += 3 * 4 ** i

        i = i+1

    return sum

print(patternToNumber('AGTC'))



