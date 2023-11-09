def boyer_moore(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = max(1, len(pattern) - i - 1)
        return table

    def good_suffix_table(pattern):
        table = [0] * len(pattern)
        last_prefix_position = len(pattern)
        for i in range(len(pattern)):
            if is_prefix(pattern, len(pattern) - i):
                last_prefix_position = len(pattern) - i
            table[i] = last_prefix_position + i - len(pattern)
        return table

    def is_prefix(pattern, p):
        j = 0
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True

    def suffix_length(pattern, p):
        length = 0
        j = len(pattern) - 1
        while p >= 0 and pattern[p] == pattern[j]:
            length += 1
            p -= 1
            j -= 1
        return length

    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)

    i = 0
    while i <= len(text) - len(pattern):
        shift = 0
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            char_shift = bad_char.get(text[i + j], len(pattern))
            if j + 1 < len(pattern):
                suffix_shift = good_suffix[j + 1]
                shift = max(char_shift, suffix_shift)
            else:
                shift = char_shift
        i += shift
    return -1

# Test the algorithm
text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"
index = boyer_moore(text, pattern)
if index != -1:
    print(f"Pattern found at index: {index}")
else:
    print("Pattern not found.")
