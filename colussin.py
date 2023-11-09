def pre_process(pattern):
    m = len(pattern)
    h = [0] * (m + 1)
    next = [0] * (m + 1)
    shift = [0] * (m + 1)

    # Preprocessing `h` and `next`
    i = m
    j = m + 1
    h[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = h[j]
        i -= 1
        j -= 1
        h[i] = j

    # Preprocessing `shift`
    i = 0
    j = h[0]
    while j <= m:
        while j <= m and shift[j] == 0:
            shift[j] = j - i
        i = j
        j = h[j]

    return shift


def colussi_search(text, pattern):
    shift = pre_process(pattern)
    m = len(pattern)
    n = len(text)
    occurrences = []

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            occurrences.append(i)
            i += shift[0]
        else:
            i += shift[j + 1]

    return occurrences


# Example usage:
text = "THIS IS A TEST TEXT"
pattern = "TEST"
result = colussi_search(text, pattern)
print("Pattern found at indices:", result)
