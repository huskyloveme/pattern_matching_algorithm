def not_so_naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0

    while i <= n - m:
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            # Khi tìm thấy chuỗi con tại vị trí i
            print("Pattern found at position", i)

        if j == 0:
            i += 1
        else:
            i += j


a = 'Not so navie aaaa'
b = 'aa'

not_so_naive_search(a,b)