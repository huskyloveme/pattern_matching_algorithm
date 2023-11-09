def brute_force_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i  # Mẫu được tìm thấy tại vị trí i trong text

    return -1  # Mẫu không được tìm thấy

# Sử dụng hàm tìm kiếm
text = "THIS IS A TEST TEXT"
pattern = "TEST"
position = brute_force_search(text, pattern)

if position != -1:
    print(f"Mẫu '{pattern}' tìm thấy ở vị trí: {position}")
else:
    print("Mẫu không được tìm thấy.")