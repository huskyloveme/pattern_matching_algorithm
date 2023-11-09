def build_shift_table(pattern):
    """
    Xây dựng bảng dịch chuyển dựa trên mẫu.
    """
    len_pattern = len(pattern)
    table = {char: len_pattern for char in pattern}
    # Lặp qua mẫu và cập nhật bước nhảy với vị trí cuối cùng từ phải qua trái
    for i in range(len_pattern - 1):
        table[pattern[i]] = len_pattern - 1 - i
    return table


def horspool_search(text, pattern):
    """
    Tìm kiếm chuỗi sử dụng thuật toán Horspool.
    """
    table = build_shift_table(pattern)
    len_pattern = len(pattern)
    len_text = len(text)

    i = 0
    while i <= len_text - len_pattern:
        shift = 0
        for j in range(len_pattern - 1, -1, -1):
            if pattern[j] != text[i + j]:
                shift = table.get(text[i + len_pattern - 1], len_pattern)
                break
        if shift == 0:
            return i  # Mẫu được tìm thấy tại vị trí i
        i += shift
    return -1  # Mẫu không được tìm thấy


# Sử dụng hàm tìm kiếm
text = "THIS IS A TEST TEXT"
pattern = "TEST"
position = horspool_search(text, pattern)

if position != -1:
    print(f"Mẫu '{pattern}' tìm thấy ở vị trí: {position}")
else:
    print("Mẫu không được tìm thấy.")
