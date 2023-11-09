def rabin_karp(text, pattern):
    # Đặt một số nguyên tố lớn để giảm thiểu xác suất va chạm hash
    prime = 101
    n, m = len(text), len(pattern)
    hpattern, htext, h = 0, 0, 1
    # Giá trị h là "pow(256, m-1) % prime"
    for i in range(m - 1):
        h = (h * 256) % prime
    # Tính giá trị hash ban đầu cho pattern và text
    for i in range(m):
        hpattern = (256 * hpattern + ord(pattern[i])) % prime
        htext = (256 * htext + ord(text[i])) % prime
    # Trượt pattern qua text
    for i in range(n - m + 1):
        # Nếu hash của pattern và text khớp, kiểm tra từng ký tự
        if hpattern == htext:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:  # Nếu không có sự khác biệt nào, một match được tìm thấy
                return i
        # Tính hash cho cửa sổ tiếp theo của text: Loại bỏ ký tự đầu tiên, thêm ký tự tiếp theo
        if i < n - m:
            htext = (256 * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Đảm bảo giá trị hash không âm
            if htext < 0:
                htext += prime
    return -1  # Không tìm thấy
# Ví dụ sử dụng
text = "THIS IS A TEST TEXT"
pattern = "TEST"
position = rabin_karp(text, pattern)
if position != -1:
    print(f"Mẫu '{pattern}' tìm thấy ở vị trí: {position}")
else:
    print("Mẫu không được tìm thấy.")
