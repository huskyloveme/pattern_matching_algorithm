def create_skip_table(pattern):
    skip_table = {}
    m = len(pattern)
    for i in range(m - 1):
        skip_table[pattern[i]] = m - i - 1
    skip_table[pattern[m - 1]] = m
    return skip_table
def skip_search(text, pattern):
    skip_table = create_skip_table(pattern)
    m = len(pattern)
    n = len(text)
    # Bắt đầu tìm kiếm từ vị trí cuối cùng của mẫu
    i = m - 1
    while i < n:
        # So sánh mẫu từ phải sang trái
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1  # Tìm thấy mẫu
        # Nhảy qua các phần tử dựa trên skip table
        i += skip_table.get(text[i], m)

    return -1  # Không tìm thấy mẫu
# Ví dụ sử dụng:
text = "this is an example where example is to be found"
pattern = "example"
result = skip_search(text, pattern)

if result != -1:
    print(f"Pattern found at index: {result}")
else:
    print("Pattern not found")
