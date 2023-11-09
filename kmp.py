def KMP_search(pattern, text):
    m, n = len(pattern), len(text)
    # Tạo bảng lps (longest proper prefix which is also suffix)
    lps = [0] * m
    compute_lps_array(pattern, m, lps)
    print(lps)
    i = j = 0  # index cho text và pattern
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            # Không khớp, chuyển j với bảng lps
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def compute_lps_array(pattern, m, lps):
    length = 0  # chiều dài của lps trước đó
    # lps[0] luôn luôn là 0
    lps[0] = 0
    i = 1
    # Tạo bảng lps
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Sử dụng thuật toán KMP
text = "asd asdxxxxccccxxxc asds asd"
pattern = "xxxxccccxxx"
KMP_search(pattern, text)
