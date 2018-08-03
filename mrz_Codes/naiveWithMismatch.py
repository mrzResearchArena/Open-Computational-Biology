def naiveWithMismatches(text, pattern, allow):
    v = []

    for i in range(len(text) - len(pattern) + 1):
        mismatch = 0
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                mismatch += 1
                if mismatch == (allow+1):
                    break
        if mismatch <= allow:
            v.append(i)

    return v


