ALPHABET_SIZE = 256


def zt_preprocess_badchar(pattern):
    m = len(pattern)
    badchar = [[-1 for _ in range(ALPHABET_SIZE)] for _ in range(m)]

    for j in range(m):
        for k in range(ALPHABET_SIZE):
            badchar[j][k] = j - pattern.rfind(chr(k), 0, j)

    return badchar


def zhu_takaoka_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n: return []  # Pattern longer than text

    # Preprocessing
    badchar = zt_preprocess_badchar(pattern)

    # Searching
    occurrences = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            occurrences.append(s)
            s += m
        else:
            bad_char_shift = badchar[j][ord(text[s + j])]
            s += max(1, bad_char_shift)

    return occurrences


# Example usage:
text = "THIS IS A TEST TEXT"
pattern = "TEST"
result = zhu_takaoka_search(text, pattern)
print("Pattern found at indices:", result)
